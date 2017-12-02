#
# Load the libraries that are used in these commands.
#
from fman import DirectoryPaneCommand, DirectoryPaneListener, show_alert, show_prompt, show_status_message, clear_status_message, load_json, save_json, clipboard

import sys, os
from fman.url import as_human_readable
from fman.url import as_url

#
# Global Variable:
#       DBDATA      All the information about the Dropbox
#                   accounts.
DBDATA = None

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
    DBDATA = load_json('DropboxConnect.json')
    if DBDATA is None:
        DBDATA = dict()
        DBDATA['Personal'] = ''
        DBDATA['Business'] = ''
        DBDATA['PersonalSecret'] = ''
        DBDATA['BusinessSecret'] = ''

#
# Function:    SaveDropBoxDataFile
#
# Description: This function saves the DBDATA dictionary
#              to the DropboxConnect.json file.
#
def SaveDropBoxDataFile():
    global DBDATA
    save_json('DropboxConnect.json',DBDATA)

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
        global DBDATA

        sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + "/dropbox-sdk-python")
        import dropbox

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
            if path_is_parent(DBDATA['Personal'],fileName):
                #
                # It's in the Personal Dropbox location.
                #
                if DBDATA['PersonalSecret'] != '':
                    #
                    # The secret has been set. Now get the path
                    # from the top of the Dropbox directory.
                    #
                    fileName = "/" + os.path.relpath(fileName,DBDATA['Personal'])
                    try:
                        #
                        # Query Dropbox for the public link.
                        #
                        client = dropbox.Dropbox(DBDATA['PersonalSecret'])
                        link = client.sharing_create_shared_link(fileName)
                        #
                        # Copy to the clipboard.
                        #
                        clipboard.set_text(link.url)
                    except:
                        #
                        # There was an error connecting to
                        # Dropbox. Tell the user.
                        #
                        show_alert("Error connecting to Dropbox:" + sys.exc_info()[0])
                else:
                    #
                    # The secret wasn't set. Tell the user.
                    #
                    show_alert("Please setup the secret for the personal Dropbox account.")
            elif path_is_parent(DBDATA['Business'],fileName):
                #
                # It's the business Dropbox location.
                #
                if DBDATA['BusinessSecret'] != '':
                    #
                    # The secret has been set. Get the path
                    # beginning at the top of the Dropbox
                    # directory.
                    #
                    fileName = os.path.relpath(fileName,DBDATA['Business'])
                    try:
                        #
                        # Query Dropbox for the public link.
                        #
                        client = dropbox.Dropbox(DBDATA['BusinessSecret'])
                        link = client.sharing_create_shared_link(fileName)
                        #
                        # Copy to the clipboard.
                        #
                        clipboard.set_text(link.url)
                    except:
                        #
                        # There was a error.
                        #
                        show_alert("Error connecting to Dropbox:" + sys.exc_info()[0])
                else:
                    #
                    # The secret hasn't been set. Tell the user.
                    #
                    show_alert("Please setup the secret for the business Dropbox account.")
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
        DBDATA['PersonalSecret'], result = show_prompt("The secret for the Personal account.")
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
        DBDATA['BusinessSecret'], result = show_prompt("The secret for the Business account.")
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
# The following function was taken from [StackOverflow](https://stackoverflow.com/questions/3812849/how-to-check-whether-a-directory-is-a-sub-directory-of-another-directory)
#
def path_is_parent(parent_path, child_path):
    # Smooth out relative path names, note: if you are concerned about symbolic links, you should use os.path.realpath too
    parent_path = os.path.abspath(parent_path)
    child_path = os.path.abspath(child_path)

    # Compare the common path of the parent and child path with the common path of just the parent path. Using the commonpath method on just the parent path will regularise the path name in the same way as the comparison that deals with both paths, removing any trailing path separator
    return os.path.commonpath([parent_path]) == os.path.commonpath([parent_path, child_path])

