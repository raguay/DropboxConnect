#
# Load the libraries that are used in these commands.
#
from fman import DirectoryPaneCommand, DirectoryPaneListener, show_alert, show_prompt, show_status_message, clear_status_message, load_json, save_json, clipboard

from fman.fs import FileSystem, exists, Column, mkdir, is_dir, move_to_trash
from fman.url import as_human_readable, as_url, splitscheme, basename, dirname
from io import UnsupportedOperation

import sys
import os
import math
from datetime import datetime

#
# In order to load the Dropbox library, we need to put the
# plugin's path into the os' sys path.
#
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(
    os.path.realpath(__file__))), "dropbox-sdk-python"))

import dropbox

#
# Global Variable:
#       DBDATA      All the information about the Dropbox
#                   accounts.
DBDATA = None
BUSCLIENT = None
PERCLIENT = None
OSSEP = os.sep

#
# Function:    ConnectToClient
#
# Description: This function creates the different client
#              connections to the Dropbox server.
#


def ConnectToClient():
    global BUSCLIENT, PERCLIENT, DBDATA

    if PERCLIENT is None:
        LoadDropBoxDataFile()
        if DBDATA['BusinessSecret'] != '':
            BUSCLIENT = dropbox.Dropbox(DBDATA['BusinessSecret'])
        if DBDATA['PersonalSecret'] != '':
            PERCLIENT = dropbox.Dropbox(DBDATA['PersonalSecret'])

#
# Function:    LoadDropBoxDataFile
#
# Description: This loads the DropboxConnect.json file
#              into the DBDATA dictionary. If the file
#              doesn't exist, it creates a default
#              dictionary.
#


def LoadDropBoxDataFile():
    global DBDATA
    if DBDATA is None:
        DBDATA = load_json('DropboxConnect.json')

        #
        # See if valid data was loaded. If not, create
        # defaults and save to the file.
        #
        if DBDATA is None:
            DBDATA = dict()
            DBDATA['Personal'] = ''
            DBDATA['Business'] = ''
            DBDATA['PersonalSecret'] = ''
            DBDATA['BusinessSecret'] = ''
            DBDATA['DefChunkSize'] = 10
            SaveDropBoxDataFile()

    #
    # Check for older installs that don't have new
    # parameters defaulted.
    #
    if 'DefChunkSize' not in DBDATA:
        DBDATA['DefChunkSize'] = 10
        SaveDropBoxDataFile()

#
# Function:    SaveDropBoxDataFile
#
# Description: This function saves the DBDATA dictionary
#              to the DropboxConnect.json file.
#


def SaveDropBoxDataFile():
    global DBDATA
    save_json('DropboxConnect.json', DBDATA)

#
# class:        GetDropboxPublicLink
#
# Description: This class determines if the file selected is
#              in a Dropbox folder areas and gets the public
#              link for it.
#


class GetDropboxPublicLink(DirectoryPaneCommand):
    #
    # This directory command is for getting the public
    # link to a Dropbox file or folder.
    #

    def __call__(self):
        global BUSCLIENT, PERCLIENT, DBDATA, OSSEP

        #
        # Get the client connections.
        #
        ConnectToClient()

        #
        # Tell the user we are generating the link in the
        # status bar. When the message is gone, they will
        # know it is in the clipboard.
        #
        show_status_message('Dropbox Link Generating')

        #
        # Get the file or directory for the link.
        #
        selected_files = self.pane.get_selected_files()
        if len(selected_files) >= 1 or (len(selected_files) == 0 and self.get_chosen_files()):
            if len(selected_files) == 0 and self.get_chosen_files():
                selected_files.append(self.get_chosen_files()[0])

            file_scheme, fileName = splitscheme(selected_files[0])
            dirNames = fileName.split(OSSEP)
            client = None
            baseName = None
            dbFileName = ''

            #
            # Determine the file scheme in use. If it is the file system,
            # make sure it's in the Dropbox folders.
            #
            if file_scheme == 'file://':
                if dirNames[3] == os.path.basename(DBDATA['Business']):
                    client = BUSCLIENT
                    baseName = DBDATA['Business']
                else:
                    client = PERCLIENT
                    baseName = DBDATA['Personal']

                sliceObj = slice(len(baseName.split(OSSEP)), len(dirNames))
                dbFileName = OSSEP + OSSEP.join(dirNames[sliceObj])
            elif file_scheme == 'dropbox://':
                if dirNames[0] == os.path.basename(DBDATA['Business']):
                    client = BUSCLIENT
                    baseName = DBDATA['Business']
                else:
                    client = PERCLIENT
                    baseName = DBDATA['Personal']
                dbFileName = OSSEP + OSSEP.join(dirNames[1:])
            else:
                raise UnsupportedOperation()

            #
            # Check for the client set properly.
            #
            if client is None:
                show_alert("Dropbox information isn't configured.")
                raise FileNotFoundError(path)

            try:
                #
                # Query Dropbox for the public link.
                #
                link = client.sharing_create_shared_link(dbFileName)
                #
                # Copy to the clipboard.
                #
                clipboard.set_text(link.url)
            except Exception as e:
                #
                # There was an error connecting to
                # Dropbox. Tell the user.
                #
                show_alert("Error connecting to Dropbox:" + str(e))
        else:
            show_alert("No files selected.")

        #
        # Clear out the status bar message.
        #
        clear_status_message()

#
# Function:    SetPersonalDB
#
# Description: This class allows the user to set the personal
#              Dropbox directory to the currently selected
#              directory.
#


class SetPersonalDB(DirectoryPaneCommand):

    def __call__(self):
        global DBDATA
        show_status_message('Dropbox Personal Directory')
        selected_files = self.pane.get_selected_files()
        if len(selected_files) >= 1 or (len(selected_files) == 0 and self.get_chosen_files()):
            if len(selected_files) == 0 and self.get_chosen_files():
                selected_files.append(self.get_chosen_files()[0])
            dirName = as_human_readable(selected_files[0])
            if os.path.isfile(dirName):
                #
                # It's a file, not a directory. Get the directory
                # name for this file's parent directory.
                #
                dirName = os.path.dirname(dirName)
            #
            # Load and save the data file.
            #
            LoadDropBoxDataFile()
            DBDATA['Personal'] = dirName
            SaveDropBoxDataFile()
        clear_status_message()

#
# Function:    SetBusinessDB
#
# Description: This class allows the user to set the business
#              Dropbox directory to the currently selected
#              directory.
#


class SetBusinessDB(DirectoryPaneCommand):

    def __call__(self):
        global DBDATA
        show_status_message('Dropbox Business Directory')
        selected_files = self.pane.get_selected_files()
        if len(selected_files) >= 1 or (len(selected_files) == 0 and self.get_chosen_files()):
            if len(selected_files) == 0 and self.get_chosen_files():
                selected_files.append(self.get_chosen_files()[0])
            dirName = as_human_readable(selected_files[0])
            if os.path.isfile(dirName):
                #
                # It's a file, not a directory. Get the directory
                # name for this file's parent directory.
                #
                dirName = os.path.dirname(dirName)
            #
            # Load and save the data file.
            #
            LoadDropBoxDataFile()
            DBDATA['Business'] = dirName
            SaveDropBoxDataFile()
        clear_status_message()


#
# Function:    SetPersonalSecret
#
# Description: This class allows the user to set the personal
#              secret for getting information from Dropbox.
#


class SetPersonalSecret(DirectoryPaneCommand):

    def __call__(self):
        global DBDATA
        show_status_message('Dropbox Personal Secret')
        LoadDropBoxDataFile()
        DBDATA['PersonalSecret'], result = show_prompt(
            "The secret for the Personal account.")
        if not result:
            DBDATA['PersonalSecret'] = ''
        SaveDropBoxDataFile()
        clear_status_message()

#
# Function:    SetBusinessSecret
#
# Description: This class allows the user to set the business
#              secret for getting information from Dropbox.
#


class SetBusinessSecret(DirectoryPaneCommand):

    def __call__(self):
        global DBDATA
        show_status_message('Dropbox Business Secret')
        LoadDropBoxDataFile()
        DBDATA['BusinessSecret'], result = show_prompt(
            "The secret for the Business account.")
        if not result:
            DBDATA['BusinessSecret'] = ''
        SaveDropBoxDataFile()
        clear_status_message()

#
# Function:    GoToPersonalDB
#
# Description: This command will take the active panel to the
#              personal Dropbox directory.
#


class GoToPersonalDB(DirectoryPaneCommand):

    def __call__(self):
        global DBDATA
        LoadDropBoxDataFile()
        if DBDATA['Personal'] != '':
            self.pane.set_path(as_url(DBDATA['Personal']))
        else:
            show_alert("Personal directory isn't set.")

#
# Function:    GoToPersonalDB
#
# Description: This command will take the active panel to the
#              personal Dropbox directory.
#


class GoToBusinessDB(DirectoryPaneCommand):

    def __call__(self):
        global DBDATA
        LoadDropBoxDataFile()
        if DBDATA['Business'] != '':
            self.pane.set_path(as_url(DBDATA['Business']))
        else:
            show_alert("Business directory isn't set.")



#
# The following function was taken from
# [StackOverflow](https://stackoverflow.com/questions/3812849/how-to-check-whether-a-directory-is-a-sub-directory-of-another-directory)
#


def path_is_parent(parent_path, child_path):
    # Smooth out relative path names, note: if you are concerned about
    # symbolic links, you should use os.path.realpath too
    parent_path = os.path.abspath(parent_path)
    child_path = os.path.abspath(child_path)

    #
    # Compare the common path of the parent and child path with the common path
    # of just the parent path. Using the commonpath method on just the parent
    # path will regularise the path name in the same way as the comparison
    # that deals with both paths, removing any trailing path separator
    #
    return os.path.commonpath([parent_path]) == os.path.commonpath([parent_path, child_path])

#
# The following code implements the Dropbox file system for fman.
#

#
# Function:    SetChunkSize
#
# Description: This class allows the user to set the chunk
#              size for uploading files to the Dropbox server.
#              The number given is in megabytes. The chunk size
#              should not be less than 4 megabytes, but not greater
#              than 140 megabytes.
#


class SetChunkSize(DirectoryPaneCommand):

    def __call__(self):
        global DBDATA
        show_status_message('Dropbox Upload Chunk Size')
        #
        # Get the current values.
        #
        LoadDropBoxDataFile()
        #
        # Get the new value from the user.
        #
        newSize, result = show_prompt(
            "Chunk Size [4-140]?")
        #
        # Check for proper results.
        #
        if not result:
            DBDATA['DefChunkSize'] = 10
        else:
            #
            # Make sure it's in the proper range.
            #
            DBDATA['DefChunkSize'] = int(newSize)
            if DBDATA['DefChunkSize'] < 4:
                DBDATA['DefChunkSize'] = 4
            elif DBDATA['DefChunkSize'] > 140:
                DBDATA['DefChunkSize'] = 140
        #
        # Save the new value.
        #
        SaveDropBoxDataFile()
        clear_status_message()


#
# Class:         DropboxUploadError
#
# Description:   This class implements the Dropbox upload error condition.
#                It's an extension of the base Exception class.
#

class DropboxUploadError(Exception):
    message = ""

    def __init__(self, message):
        self.message = message


#
# Class:       GoToDropboxFileSystem
#
# Description: This directory command will open the top of the Dropbox
#              directory structure to the current panel. This allows
#              the user to go to that file system.
#


class GoToDropboxFileSystem(DirectoryPaneCommand):

    def __call__(self):
        self.pane.set_path('dropbox://')


#
# Class:        DropBoxFileSystem
#
# Description:  This class implements the Dropbox file system. It is
#               a subclass of the FileSystem class.
#


class DropBoxFileSystem(FileSystem):

    scheme = 'dropbox://'

    #
    # Function:      iterdir
    #
    # Description:   This function is the main working function for the
    #                Dropbox file system. Here is where Dropbox is queried
    #                for information about the files in Dropbox. The
    #                information is then cached and used in all the other
    #                functions.
    #
    #
    #
    def iterdir(self, path):
        #
        # Load in the Dropbox data files if not already loaded.
        #
        global BUSCLIENT, PERCLIENT, DBDATA, OSSEP

        #
        # Process dependently on the path given.
        #
        if path == '':
            #
            # It's the top. Show the different Dropbox directories setup.
            #
            LoadDropBoxDataFile()
            if DBDATA['Business'] != '':
                name = os.path.basename(DBDATA['Business'])
                self.cache.put(name, "Name", name)
                self.cache.put(name, "Size", '')
                self.cache.put(name, "isDir", True)
                yield name
            if DBDATA['Personal'] != '':
                name = os.path.basename(DBDATA['Personal'])
                self.cache.put(name, "Name", name)
                self.cache.put(name, "Size", '')
                self.cache.put(name, "isDir", True)
                yield name
        else:
            #
            # Get the directory contents from Dropbox.
            #
            show_status_message("Loading Dropbox information...")
            dirNames = path.split(OSSEP)
            ConnectToClient()
            client = None
            if dirNames[0] == os.path.basename(DBDATA['Business']):
                client = BUSCLIENT
            else:
                client = PERCLIENT

            if client is None:
                show_alert("Dropbox information isn't configured.")
                raise FileNotFoundError(path)

            #
            # List the directory.
            #
            joinedPath = ''
            if len(dirNames[1:]) > 0:
                joinedPath = OSSEP + OSSEP.join(dirNames[1:])

            curDirList = self.cache.query(path, "entries", lambda: client.files_list_folder(path=joinedPath, recursive=False))
            self.cache.put(path, "Name", dirNames[-1])
            self.cache.put(path, "Size", "")
            self.cache.put(path, "isDir", True)
            self.cache.put(path, "synced", IsPathSynced(as_url(path)))
            for file in curDirList.entries:
                size = ''
                isDir = True
                if not isinstance(file, dropbox.files.FolderMetadata):
                    size = file.size
                    isDir = False
                self.cache.put(path + OSSEP + file.name, "Name", file.name)
                self.cache.put(path + OSSEP + file.name, "Size", size)
                self.cache.put(path + OSSEP + file.name, "isDir", isDir)
                self.cache.put(path + OSSEP + file.name, "synced", IsPathSynced(as_url(path + OSSEP + file.name)))
                yield file.name
            clear_status_message()

    def is_dir(self, path):
        #
        # Load in the Dropbox data files if not already loaded.
        #
        global DBDATA

        #
        # Make sure we are connected.
        #
        LoadDropBoxDataFile()

        #
        # Get the right thing based on the path.
        #
        isADir = False
        if path == '':
            #
            # The topmost is a directory.
            #
            isADir = True
        elif path == os.path.basename(DBDATA['Business']):
            #
            # The Business Dropbox is a directory.
            #
            isADir = True
        elif path == os.path.basename(DBDATA['Personal']):
            #
            # The Personal Dropbox is a directory.
            #
            isADir = True
        else:
            #
            # Everything else, we need to get from Dropbox. use
            # the last query information to determine if it is
            # a directory.
            #
            isADir = self.cache.query(path, "isDir", lambda: False)
        return isADir

    def size_bytes(self, path):
        result = self.cache.query(path, "Size", lambda: None)
        if result is None:
            raise FileNotFoundError(path)
        else:
            return result

    def name(self, path):
        result = self.cache.query(path, "Name", lambda: None)
        if result is None:
            raise FileNotFoundError(path)
        else:
            return result

    def get_default_columns(self, path):
        return ('core.Name', 'core.Size', 'dropboxconnect.Synced')

    def copy(self, src, dst):
        #
        # No root copying.
        #
        if src == '' or dst == '':
            raise UnsupportedOperation()

        src_scheme, src_path = splitscheme(src)
        dst_scheme, dst_path = splitscheme(dst)
        if src_scheme == 'dropbox://' and dst_scheme == 'file://':
            #
            # Tell the user what we are doing.
            #
            show_status_message("Copying from Dropbox to Filesystem...")

            try:
                #
                # Determine if it is a directory or a file.
                #
                if self.cache.query(src_path, "isDir", lambda: None) == True:
                    #
                    # This will copy a directory.
                    #
                    self.copyDropboxDirToFilesystem(src_path, dst_path)
                else:
                    #
                    # This copies a single file.
                    #
                    self.copyDropboxFileToFilesystem(src_path, dst_path)
            except:
                #
                # An error. Tell the user.
                #
                show_alert("Unable to Download from Dropbox. Network Error.")

            #
            # Clear the status message.
            #
            clear_status_message()
        elif src_scheme == 'file://' and dst_scheme == 'dropbox://':
            #
            # Upload the file. Tell the user about it.
            #
            show_status_message("Upload to Dropbox...")

            try:
                #
                # Determine if it is a directory or a file.
                #
                if is_dir(src):
                    #
                    # This will copy a directory.
                    #
                    self.copyFilesystemDirToDropbox(src_path, dst_path)
                else:
                    #
                    # This copies a single file.
                    #
                    self.copyFilesystemFileToDropbox(src_path, dst_path)
            except:
                show_alert("Couldn't upload to Dropbox. Network error.")

            #
            # Clear out the status message.
            #
            clear_status_message()
        else:
            #
            # If you get here, it is a condition that fman should handle.
            #
            raise UnsupportedOperation()

    def copyDropboxDirToFilesystem(self, src_path, dst_path):
        global OSSEP
        mkdir(as_url(dst_path))
        for fileName in self.iterdir(src_path):
            self.copy("dropbox://" + src_path + OSSEP + fileName, as_url(dst_path + OSSEP + fileName))

    def copyDropboxFileToFilesystem(self, src_path, dst_path):
        global DBDATA, BUSCLIENT, PERCLIENT, OSSEP

        ConnectToClient()
        srcDirNames = src_path.split(OSSEP)
        client = None
        if srcDirNames[0] == os.path.basename(DBDATA['Business']):
            client = BUSCLIENT
        else:
            client = PERCLIENT

        if client is None:
            show_alert("Dropbox information isn't configured.")
            raise DropboxUploadError(path)

        dbFileLoc = OSSEP + OSSEP.join(srcDirNames[1:])
        if dbFileLoc == OSSEP:
            show_alert("Can't Copy the whole file system!")
            raise DropboxUploadError()

        try:
            client.files_download_to_file(dst_path, dbFileLoc)
        except Exception as e:
            print(e)
            raise DropboxUploadError()

    def copyFilesystemDirToDropbox(self, src_path, dst_path):
        global OSSEP
        #
        # Add directory to the cache.
        #
        self.cache.put(dst_path, "Name", os.path.basename(dst_path))
        self.cache.put(dst_path, "Size", None)
        self.cache.put(dst_path, "isDir", True)
        self.cache.put(dst_path, "synced", False)

        for fileName in os.listdir(src_path):
            self.copy(as_url(src_path + OSSEP + fileName), "dropbox://" + dst_path + OSSEP + fileName)

    def copyFilesystemFileToDropbox(self, src_path, dst_path):
        global DBDATA, BUSCLIENT, PERCLIENT, OSSEP

        ConnectToClient()

        dstDirNames = dst_path.split(OSSEP)
        client = None
        if dstDirNames[0] == os.path.basename(DBDATA['Business']):
            client = BUSCLIENT
        else:
            client = PERCLIENT

        if client is None:
            show_alert("Dropbox information isn't configured.")
            raise FileNotFoundError(path)

        dbFileLoc = OSSEP + OSSEP.join(dstDirNames[1:])
        file_size = None
        try:
            f = open(src_path, 'rb')
            file_size = os.path.getsize(src_path)
            CHUNK_SIZE = DBDATA['DefChunkSize'] * 1024 * 1024

            if file_size <= CHUNK_SIZE:
                client.files_upload(f.read(), dbFileLoc)

            else:
                upload_session_start_result = client.files_upload_session_start(f.read(CHUNK_SIZE))
                cursor = dropbox.files.UploadSessionCursor(session_id=upload_session_start_result.session_id, offset=f.tell())
                commit = dropbox.files.CommitInfo(path=dbFileLoc)

                while f.tell() < file_size:
                    prevLoc = f.tell()
                    chunk = f.read(CHUNK_SIZE)
                    try:
                        if ((file_size - f.tell()) <= CHUNK_SIZE):
                            client.files_upload_session_finish(chunk, cursor, commit)
                        else:
                            client.files_upload_session_append(chunk,cursor.session_id, cursor.offset)
                            cursor.offset = f.tell()
                    except:
                        #
                        # Usually a timeout error. Try lowering the chunk
                        # size. This will lower the likely hood of a
                        # timeout error.
                        #
                        f.seek(prevLoc)
                        CHUNK_SIZE = CHUNK_SIZE - math.floor(CHUNK_SIZE/4)
                        if CHUNK_SIZE < 1024:
                            raise DropboxUploadError("Upload Failed.")
                        else:
                            continue
            #
            # Add new file to the cache.
            #
            self.cache.put(dst_path, "Name", dstDirNames[-1])
            self.cache.put(dst_path, "Size", file_size)
            self.cache.put(dst_path, "isDir", False)
            self.cache.put(dst_path, "synced", False)

            #
            # Close the file.
            #
            f.close()
        except Exception as e:
            print(e)
            if f is not None:
                f.close()
            raise FileNotFoundError()

    def exists(self, url):
        if url == '':
            return True
        else:
            return self.cache.query(url, "Name", lambda: None) is not None

    def move(self, src, dst):
        global DBDATA, BUSCLIENT, PERCLIENT, OSSEP
        #
        # No root moving.
        #
        if src == '' or dst == '':
            raise UnsupportedOperation()

        src_scheme, src_path = splitscheme(src)
        dst_scheme, dst_path = splitscheme(dst)
        if src_scheme == 'dropbox://' and dst_scheme == 'file://':
            #
            # Tell the user what we are doing.
            #
            show_status_message("Moving from Dropbox to Filesystem...")

            try:
                #
                # Determine if it is a directory or a file.
                #
                if self.cache.query(src_path, "isDir", lambda: None) == True:
                    #
                    # This will copy a directory.
                    #
                    self.copyDropboxDirToFilesystem(src_path, dst_path)
                else:
                    #
                    # This copies a single file.
                    #
                    self.copyDropboxFileToFilesystem(src_path, dst_path)
                #
                # Now, delete the file.
                #
                self.delete(src_path)
            except:
                #
                # An error. Tell the user.
                #
                show_alert("Unable to Download from Dropbox. Network Error.")

            #
            # Clear the status message.
            #
            clear_status_message()
        elif src_scheme == 'file://' and dst_scheme == 'dropbox://':
            #
            # Upload the file. Tell the user about it.
            #
            show_status_message("Upload to Dropbox...")

            try:
                #
                # Determine if it is a directory or a file.
                #
                if is_dir(src):
                    #
                    # This will copy a directory.
                    #
                    self.copyFilesystemDirToDropbox(src_path, dst_path)
                else:
                    #
                    # This copies a single file.
                    #
                    self.copyFilesystemFileToDropbox(src_path, dst_path)
                #
                # Now, delete the source.
                #
                move_to_trash(src)
            except:
                show_alert("Couldn't upload to Dropbox. Network error.")

            #
            # Clear out the status message.
            #
            clear_status_message()
        elif (src_scheme == dst_scheme) and (src_scheme == 'dropbox://'):
            #
            # Make sure we have a Dropbox connection.
            #
            ConnectToClient()

            #
            # Get the right client for the account.
            #
            dstDirNames = dst_path.split(OSSEP)
            client = None
            if dstDirNames[0] == os.path.basename(DBDATA['Business']):
                client = BUSCLIENT
            else:
                client = PERCLIENT

            if client is None:
                #
                # Client not created. Not all the information
                # connecting to Dropbox is setup.
                #
                show_alert("Dropbox information isn't configured.")
                raise FileNotFoundError(path)

            #
            # This is a rename or move operation within Dropbox.
            #
            dstDirNames = dst_path.split(OSSEP)
            srcDirNames = src_path.split(OSSEP)
            if dstDirNames[0] == srcDirNames[0]:
                #
                # This is a rename or move within the current Dropbox
                # file system.
                #
                try:
                    #
                    # Create the proper location within Dropbox.
                    #
                    dstdbFileLoc = OSSEP + OSSEP.join(dstDirNames[1:])
                    srcdbFileLoc = OSSEP + OSSEP.join(srcDirNames[1:])

                    #
                    # Move the file.
                    #
                    client.files_move(srcdbFileLoc, dstdbFileLoc)

                    #
                    # Fix the cache.
                    #
                    newName = os.path.basename(dst_path)
                    self.cache.put(dst_path, "Name", newName)
                    self.cache.put(dst_path, "isDir", self.cache.query(src_path, "isDir", lambda: None))
                    self.cache.put(dst_path, "synced", None)
                    self.cache.put(dst_path, "Size", self.cache.query(src_path, "Size", lambda: None))
                    self.cache.put(src_path, "Name", newName)
                except Exception as e:
                    #
                    # There was a network error.
                    #
                    print(e)
                    raise DropboxUploadError("Move Failed.")
            else:
                #
                # This is a move from one Dropbox account to another
                # Dropbox account. Need to download and re-upload.
                #
                raise UnsupportedOperation()
        else:
            #
            # If you get here, it is a condition that fman should handle.
            # This is a move from/to Dropbox to another non-native file
            # system.
            #
            raise UnsupportedOperation()

    def delete(self, file_path):
        global DBDATA, BUSCLIENT, PERCLIENT, OSSEP

        #
        # Get the client connection.
        #
        ConnectToClient()

        #
        # Get the correct client.
        #
        dstDirNames = file_path.split(OSSEP)
        client = None
        if dstDirNames[0] == os.path.basename(DBDATA['Business']):
            client = BUSCLIENT
        else:
            client = PERCLIENT

        if client is None:
            show_alert("Dropbox information isn't configured.")
            raise DropboxUploadError(path)

        #
        # Create the correct path in Dropbox.
        #
        dbFileLoc = OSSEP + OSSEP.join(dstDirNames[1:])
        try:
            #
            # Delete the file or directory from DropBox.
            #
            client.files_delete(dbFileLoc)
            #
            # Remove it from the cache.
            #
            self.cache.put(file_path, "Name", None)
        except:
            #
            # There was a network error.
            #
            raise DropboxUploadError()

    def move_to_trash(self, file_url):
        #
        # There isn't a "trash" in Dropbox. Just delete it.
        #
        self.delete(file_url)

    def mkdir(self, dir_url):
        global DBDATA, BUSCLIENT, PERCLIENT, OSSEP

        #
        # Make sure it doesn't already exist first.
        #
        if self.cache.query(dir_url, "isDir", lambda: None) is None:
            #
            # Make sure we have a Dropbox connection.
            #
            ConnectToClient()

            #
            # Get the right connection for the Dropbox being used.
            #
            dstDirNames = dir_url.split(OSSEP)
            client = None
            if dstDirNames[0] == os.path.basename(DBDATA['Business']):
                client = BUSCLIENT
            else:
                client = PERCLIENT

            if client is None:
                show_alert("Dropbox information isn't configured.")
                raise FileNotFoundError(path)

            #
            # Create the correct Dropbox location.
            #
            dbFileLoc = OSSEP + OSSEP.join(dstDirNames[1:])
            try:
                #
                # Create the folder.
                #
                client.files_create_folder(dbFileLoc)

                #
                # Update the cache.
                #
                self.cache.put(dir_url, "Name", dstDirNames[-1])
                self.cache.put(dir_url, "isDir", True)
                self.cache.put(dir_url, "Size", '')
            except:
                raise FileNotFoundError(dir_url)
        else:
            raise FileExistsError(dir_url)

    def touch(self, file_url):
        print("Touch the file: " + file_url)

    def modified_datetime(self, path):
        return self.cache.query(path, "ModifiedDT", lambda: datetime.now())

#
# Function:    DropboxPathToLocalPath
#
# Description: This function finds the local path for a
#              synced Dropbox location.
#
# Inputs:
#              path     The path in the Dropbox file system.
#


def DropboxPathToLocalPath(path):
    #
    # Get the global data and set the default.
    #
    global DBDATA, OSSEP
    scheme, dirNames = splitscheme(path)
    dirNames = dirNames.split(OSSEP)

    #
    # determine the results.
    #
    pathParts = []
    if dirNames[0] == os.path.basename(DBDATA['Business']):
        pathParts.append(DBDATA['Business'])
    elif dirNames[0] == os.path.basename(DBDATA['Personal']):
        pathParts.append(DBDATA['Personal'])
    pathParts += dirNames[1:]
    return as_url(OSSEP.join(pathParts))

#
# Function:    IsPathSynced
#
# Description: This function determines if the Dropbox location
#              is currently synced to the local file system.
#
# Inputs:
#              path     The path in the Dropbox file system.
#


def IsPathSynced(path):
    if exists(DropboxPathToLocalPath(path)):
        return '   🔄'
    else:
        return ''

#
# Class:        Synced
#
# Description:  This class extends the Column class in fman for
#               creating the Synced custom column in fman.
#


class Synced(Column):
    def get_str(self, url):
        return str(self.get_sort_value(url))

    def get_sort_value(self, url, is_ascending=True):
        return IsPathSynced(url)
