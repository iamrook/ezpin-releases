# EZPin downloads

EZPin adds Pinterest Save buttons to eligible images on WordPress posts, pages, and products. Readers save images to their own Pinterest accounts through a compact popup.

**[Download the latest EZPin release](https://github.com/iamrook/ezpin-releases/releases/latest)**

Choose **ezpin-VERSION.zip** under **Assets**. Upload it through **WordPress → Plugins → Add New → Upload Plugin**, then activate EZPin. Requires WordPress 6.2+ and PHP 7.4+.

GitHub's automatic “Source code” downloads contain this distribution repository, not an installable plugin. Use the named release ZIP.

## Updates

Active installations of EZPin 1.1.0 or later receive updates in the normal WordPress dashboard. Automatic installation is optional and controlled by each site owner. No GitHub account or access token is required. To refresh immediately, use **Dashboard → Updates → Check again**.

Versions 1.0.2 and earlier need one manual ZIP upload, choosing to replace the installed plugin. Saved settings and image/page metadata are retained. Inactive copies need reactivation or a manual ZIP update.

The updater downloads release metadata from this repository and verifies the release ZIP's SHA-256 before installation. GitHub receives update/download requests from the WordPress server; see GitHub's [privacy policy](https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement).

## Features and limitations

- Desktop hover buttons and mobile Save controls.
- Button placement, image-size thresholds, and content exclusions.
- Per-page and per-image Pinterest descriptions, destinations, and alternate images.
- Keyboard access and preservation of image alt text.

Pinterest controls authentication, board selection, and final Pin titles. EZPin cannot guarantee a separate title on a saved Pin. It does not load Pinterest tracking scripts or require Pinterest API credentials.

## Repository contents

This repository hosts public release packages, update metadata, and the publication workflow. Development history, tests, and work in progress remain in a separate private repository. The ZIP includes the PHP and JavaScript needed to run the plugin, under GPL-2.0-or-later; keeping the development repository private does not hide code distributed inside the plugin.

The `codex/releases` branch holds the current distribution files. Stable tags publish verified ZIP assets. Only complete release ZIPs and their metadata are promoted after the private project's tests pass. Published versions are not overwritten; corrections use a new version.

For support, [open an issue](https://github.com/iamrook/ezpin-releases/issues). EZPin is maintained by OddityMall and is not affiliated with Pinterest.
