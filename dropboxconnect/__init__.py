#
# Load the libraries that are used in these commands.
#
from fman import DirectoryPaneCommand, DirectoryPaneListener, show_alert, show_prompt, show_status_message, clear_status_message, load_json, save_json, clipboard

from fman.fs import FileSystem, UnsupportedOperation, exists, Column
from fman.url import as_human_readable, as_url, splitscheme

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(
    os.path.realpath(__file__))) + "/dropbox-sdk-python")

import dropbox

#
# Global Variable:
#       DBDATA      All the information about the Dropbox
#                   accounts.
DBDATA = None
BUSCLIENT = None
PERCLIENT = None


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
        if DBDATA is None:
            DBDATA = dict()
            DBDATA['Personal'] = ''
            DBDATA['Business'] = ''
            DBDATA['PersonalSecret'] = ''
            DBDATA['BusinessSecret'] = ''
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
# Function:    GetDropboxPublicLink
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
        global BUSCLIENT, PERCLIENT, DBDATA

        ConnectToClient()

        #
        # Tell the user we are generating the link in the
        # status bar. When the message is gone, they will
        # know it is in the clipboard.
        #
        show_status_message('Dropbox Link Generating')
        #
        # Get the Global Data from it's json file.
        #
        LoadDropBoxDataFile()
        #
        # Get the file or directory for the link.
        #
        selected_files = self.pane.get_selected_files()
        if len(selected_files) >= 1 or (len(selected_files) == 0 and self.get_chosen_files()):
            if len(selected_files) == 0 and self.get_chosen_files():
                selected_files.append(self.get_chosen_files()[0])
            fileName = as_human_readable(selected_files[0])
            #
            # See if the file is in a Dropbox location.
            #
            if path_is_parent(DBDATA['Personal'], fileName):
                #
                # It's in the Personal Dropbox location.
                #
                if DBDATA['PersonalSecret'] != '':
                    #
                    # The secret has been set. Now get the path
                    # from the top of the Dropbox directory.
                    #
                    fileName = "/" + \
                        os.path.relpath(fileName, DBDATA['Personal'])
                    try:
                        #
                        # Query Dropbox for the public link.
                        #
                        link = PERCLIENT.sharing_create_shared_link(fileName)
                        #
                        # Copy to the clipboard.
                        #
                        clipboard.set_text(link.url)
                    except:
                        #
                        # There was an error connecting to
                        # Dropbox. Tell the user.
                        #
                        show_alert("Error connecting to Dropbox:" +
                                   sys.exc_info()[0])
                else:
                    #
                    # The secret wasn't set. Tell the user.
                    #
                    show_alert(
                        "Please setup the secret for the personal Dropbox account.")
            elif path_is_parent(DBDATA['Business'], fileName):
                #
                # It's the business Dropbox location.
                #
                if DBDATA['BusinessSecret'] != '':
                    #
                    # The secret has been set. Get the path
                    # beginning at the top of the Dropbox
                    # directory.
                    #
                    fileName = "/" + \
                        os.path.relpath(fileName, DBDATA['Business'])
                    try:
                        #
                        # Query Dropbox for the public link.
                        #
                        link = BUSCLIENT.sharing_create_shared_link(fileName)
                        #
                        # Copy to the clipboard.
                        #
                        clipboard.set_text(link.url)
                    except:
                        #
                        # There was a error.
                        #
                        show_alert("Error connecting to Dropbox:" +
                                   sys.exc_info()[0])
                else:
                    #
                    # The secret hasn't been set. Tell the user.
                    #
                    show_alert(
                        "Please setup the secret for the business Dropbox account.")
            else:
                #
                # It's not a Dropbox file. Tell the user.
                #
                show_alert("The file isn't in a Dropbox area.")
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
# Function:    GoToDropboxFileSystem
#
# Description: This directory command will open the top of the Dropbox
#              directory structure to the current panel. This allows
#              the user to go to that file system.
#


class GoToDropboxFileSystem(DirectoryPaneCommand):

    def __call__(self):
        self.pane.set_path('dropbox://')


class DropBoxFileSystem(FileSystem):

    scheme = 'dropbox://'

    def iterdir(self, path):
        #
        # Load in the Dropbox data files if not already loaded.
        #
        global BUSCLIENT, PERCLIENT, DBDATA

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
            dirNames = path.split('/')
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
                joinedPath = "/" + "/".join(dirNames[1:])

            def _getDropboxFiles():
                return client.files_list_folder(path=joinedPath, recursive=False)

            curDirList = self.cache.query(path, "entries", _getDropboxFiles)
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
                self.cache.put(path + "/" + file.name, "Name", file.name)
                self.cache.put(path + "/" + file.name, "Size", size)
                self.cache.put(path + "/" + file.name, "isDir", isDir)
                self.cache.put(path + "/" + file.name, "synced", IsPathSynced(as_url(path + "/" + file.name)))
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
            def _returnFalse():
                return False
            isADir = self.cache.query(path, "isDir", _returnFalse)
        return isADir

    def size_bytes(self, path):
        def _returnEmpty():
            return None
        result = self.cache.query(path, "Size", _returnEmpty)
        if result is None:
            raise FileNotFoundError(path)
        else:
            return result

    def name(self, path):
        def _returnEmpty():
            return None
        result = self.cache.query(path, "Name", _returnEmpty)
        if result is None:
            raise FileNotFoundError(path)
        else:
            return result

    def get_default_columns(self, path):
        return ('core.Name', 'core.Size', 'dropboxconnect.Synced')
#        return ('core.Name', )

    def copy(self, src, dst):
        if src == '' or dst == '':
            return

        src_scheme, src_path = splitscheme(src)
        dst_scheme, dst_path = splitscheme(dst)
        if src_scheme == 'dropbox://' and dst_scheme == 'file://':
            #
            # Download the file.
            #
            show_alert("Download: Copy from " + src + " to " + dst)
        elif src_scheme == 'file://' and dst_scheme == 'dropbox://':
            #
            # Upload the file.
            #
            show_alert("Upload: Copy from " + src + " to " + dst)
        elif src_scheme == dst_scheme:
            #
            # Dropbox to Dropbox copy.
            #
            show_alert("Acrossload: Copy from " + src + " to " + dst)
        else:
            raise UnsupportedOperation()

    def move(self, src, dst):
        if src == '' or dst == '':
            return

        src_scheme, src_path = splitscheme(src)
        dst_scheme, dst_path = splitscheme(dst)
        if src_scheme == 'dropbox://' and dst_scheme == 'file://':
            #
            # Download the file and delete it off of Dropbox.
            #
            show_alert("Download & Delete: Move from " + src + " to " + dst)
        elif src_scheme == 'file://' and dst_scheme == 'dropbox://':
            #
            # Upload the file and delete from file system.
            #
            show_alert("Upload & Delete: Move from " + src + " to " + dst)
        elif src_scheme == dst_scheme:
            #
            # Dropbox to Dropbox copy and then delete original.
            #
            show_alert("Acrossload & Delete: Move from " + src + " to " + dst)
        else:
            raise UnsupportedOperation()

    def delete(self, file_url):
        show_alert("Delete the file: " + file_url)

    def move_to_trash(self, file_url):
        show_alert("Trash the file: " + file_url)

    def mkdir(self, dir_url):
        show_alert("Make the directory: " + dir_url)

    def touch(self, file_url):
        show_alert("Touch the file: " + file_url)

#    def resolve(self, file_url):
#        return(file_url)

#    def resolve(self, path):
#        return resolved_path

def IsPathSynced(path):
    #
    # Get the global data and set the default.
    #
    global DBDATA
    result = ''
    scheme, dirNames = splitscheme(path)
    dirNames = dirNames.split("/")
    print("\nStarting to check....\n")

    #
    # determine the results.
    #
    pathParts = []
    if dirNames[0] == os.path.basename(DBDATA['Business']):
        pathParts.append(DBDATA['Business'])
    elif dirNames[0] == os.path.basename(DBDATA['Personal']):
        pathParts.append(DBDATA['Personal'])
    else:
        raise FileNotFoundError(path)
    pathParts += dirNames[1:]
    if exists(as_url("/".join(pathParts))):
        result = '   🔄'

    #
    # return the result.
    #
    return result

class Synced(Column):
    def get_str(self, url):
        return str(self.get_sort_value(url))

    def get_sort_value(self, url, is_ascending=True):
        return IsPathSynced(url)
