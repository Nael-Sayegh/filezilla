# FileZilla

* Author: Nael Sayegh
* URL: [infos@nael-accessvision.com](mailto:infos@nael-accessvision.com)
* Download the [stable version][1] ;
<!-- * Download the [Latest version on Nael-AccessVision.com](https://) ; -->
* NVDA Compatibility: 2021.3 and above ;
* [Source code on GitHub][2] ;

# Presentation

This module brings improvements to the FileZilla software by adding keyboard shortcuts and missing labels on buttons.

## Shortcuts

  * ctrl+shift+h: Moves to the connection history button
  * CTRL+f6: Switches between the remote and local file lists; when not focused on a list, it moves to the remote file list
  * nvda+ctrl+alt+F: Manually checks for module updates (works outside of FileZilla)
  * nvda+ctrl+alt+shift+F: Enables/disables automatic update checking (works outside of FileZilla)

## Labels

This module adds the following labels in the software

  * Adds the Connection History label to the button after the Quick Connect button.
  * Adds the Search Options label in the remote file search field
  * Adds the Close Search label in the remote file field.

## Changes

### Version 2024.03.27

  * Improvement of the update system and removal of keyboard shortcuts related to updates.

### Version 2024.03.21

  * Error correction when proposing an update.

### Version 2024.03.20

  * Check if a version of FileZilla is detected; otherwise, an error message is displayed when using Ctrl+F6.

### Version 2024.01.20

  * Adding a button "What's new" in the update dialog too see new features before to do an update

### Version 2023.12.22

  * Adding compatibility with NVDA 2024.1

### Version 2023.10.08
  * Fixed the tab shortcut to exit the connection status area, which was not always working.

### Version 2023.10.03
  * Added support for FileZilla 3.65 while maintaining compatibility with previous versions
  * Modified keyboard shortcut, now when you are on one of the file lists, you can use ctrl+f6 to switch between lists. When not on any list, the shortcut takes you to the remote file list

### Version 2023.06.23
  * Fixed minor bugs

### Version 2023.06.18
  * Added the ability to change the tab and escape shortcuts to switch between lists
  * Fixed an issue with the update program

### Version 2023.06.17
  * First version

Copyright ©: 2024 (Nael Sayegh and Nael-Accessvision)

<!-- links section -->

[1]: https://github.com/nael-sayegh/filezilla/releases/download/2024.03.27/filezilla-2024.03.27.nvda-addon

[2]: https://github.com/nael-sayegh/filezilla