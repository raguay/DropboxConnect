## Dropbox Connect

Plugin for [fman.io](https://fman.io) that allows you to perform actions on your Dropbox files.

You can install this plugin by pressing `<shift+cmd+p>` to open the command pallet. Then type `install plugin`. Look for the `DropboxConnect` plugin and select it.

After restarting **fman**, you will have the ability to get a public link to a file in your Dropbox personal or business account.

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

#### Files Created and Used

`DropboxConnect.json`

This file contains the directory location and the secrets for the personal and business Dropbox accounts.

#### Suggested Usage

Once the plugin is installed, set the Dropbox directories by having the cursor on the personal Dropbox directory and run the command `set personal db` in the command prompt. Do the same with the business directory.

Next, log into your Dropbox account in a web browser, go to the settings page, scroll to the bottom and select 'Developers'. On the Developer page, select the 'My Apps' link. Select the 'Create app' link on the 'App Console' page. Fill out the form with the following selections: 'Dropbox API', and 'Full Dropbox'. The name can be anything you want. I used "fmanConnectP". Then select 'Personal', and 'Create app'.

Dropbox will then have you on the new apps page. Scroll down to 'Generate access token' and select 'Generate'. Copy the alphanumeric token given. In fman, run the `set personal secret` and give it this token. Do the same for the business account if you have one.

Now you can select any file in a Dropbox directry and use the `get Dropbox public link` command or `<shift>+<ctrl>+d` hotkey. The public link will be copied to the clipboard.

### Features

- Get a public sharable link for a file or directory from Dropbox.
