## Dropbox Connect

Plugin for [fman.io](https://fman.io) that allows you to perform actions on your Dropbox files. This plugin also contains the Dropbox file system for interacting with your Dropbox accounts just like your local disk. Currently, only browsing and copying files/directories from the cloud server to the local file system is implemented. The browsing shows the file/directory names, size of the files only, and an 🔄 if it is synced to your file system. I'm working on copy, move, delete, and getting the public link for files in the Dropbox filesystem.

You can install this plugin by pressing `<shift+cmd+p>` to open the command pallet. Then type `install plugin`. Look for the `DropboxConnect` plugin and select it.

After restarting **fman**, you will have the ability to get a public link to a file in your Dropbox personal or business account.

#### Setup

Once the plugin is installed, set the Dropbox directories by having the cursor on the personal Dropbox directory and run the command `set personal db` in the command prompt. Do the same with the business directory.

Next, log into the [App Console](https://www.dropbox.com/developers/apps) of your Dropbox account in a web browser. Select the 'Create app' link on the 'App Console' page. Fill out the form with the following selections: 'Dropbox API', and 'Full Dropbox'. The name can be anything you want. I used "fmanConnectP". Then select 'Personal', and 'Create app'.

Dropbox will then have you on the new apps page. Scroll down to 'Generate access token' and select 'Generate'. Copy the alphanumeric token given. In fman, run the `set personal secret` and give it this token. Do the same for the business account if you have one.

Now you can select any file in a Dropbox directry and use the `get Dropbox public link` command or `<shift>+<ctrl>+d` hotkey. The public link will be copied to the clipboard.

You can also use the `go_to_dropbox_file_system` command to browse the cloud server and copy files/directories from the Dropbox cloud to your local file system. More to come!

### Usage

#### HotKeys Set

`<shift>+<ctrl>+d`

- Get a public link for the current file or dirctory.

#### Commands

`get_dropbox_public_link`

- This command will take the current file or directory and get a public shared link to the file in Dropbox.

`set_business_secret`

- This command is used to set the secret for the business account.

`set_personal_secret`

- This command is used to set the secret for the personal account.

`set_business_db`

- This command sets the current directory if the cursor is on a file or the directory the cursor is on to the business account Dropbox folder.

`set_personal_db`

- This command sets the current directory if the cursor is on a file or the directory the cursor is on to the personal account Dropbox folder.

`go_to_personal_db`

- This command will go to the directory set for the personal Dropbox.

`go_to_business_db`

- This command will go to the directory set for the business Dropbox.

`go_to_dropbox_file_system`

This command will open the current panel in the Dropbox file system. Currently, only browsing and copying from the cloud to the local file system is implemented. This is still a work in progress.

#### Files Created and Used

`DropboxConnect.json`

This file contains the directory location and the secrets for the personal and business Dropbox accounts.

### Features

- Get a public sharable link for a file or directory from Dropbox.
- Browse the Dropbox files from the cloud server.
- Full copying of files/directories from cloud to local file system works.

