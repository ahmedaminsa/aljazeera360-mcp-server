> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/vesper-insights/secure-data-file-transfer-guide/creating-a-pgp-key.md).

# Creating a PGP Key

### Requirements

Here we present the steps necessary to install the software required to operate with encrypted files for **Mac**, **Windows** and **Linux**

#### **Mac**  <a href="#mac-mediainline" id="mac-mediainline"></a>

We recommend you use [![](https://gpgtools.org/favicon-16.png)GPG Suite](https://gpgtools.org/). Download and follow the instructions provided by the installer.

#### Windows  <a href="#windows-mediainline" id="windows-mediainline"></a>

We recommend you use[![](https://gpg4win.org/favicon.png)Gpg4win - Get Gpg4win](https://gpg4win.org/get-gpg4win.html). Download and follow the instructions provided by the installer.

#### Linux <a href="#linux-mediainline" id="linux-mediainline"></a>

Install [![](https://gnupg.org/favicon.ico)The GNU Privacy Guard](https://gnupg.org/) cli using your favourite package manager. We will assume you are using Ubuntu’s **APT** package manager, but the steps should be similar if you use another package manager.

`sudo apt-get install gnupg`

### Creating a public PGP key

#### **Mac**  <a href="#mac-mediainline-.1" id="mac-mediainline-.1"></a>

1. Open [![](https://gpgtools.org/favicon-16.png)GPG Suite](https://gpgtools.org/), you should see any keys already imported into your system. By default you will always see 2 **public** keys from `@gpgtools.org`
2. Click on the plus sign ![:heavy\_plus\_sign:](https://dicetech.atlassian.net/gateway/api/emoji/dcf7b88b-ff0d-41e1-8a6c-06f28edfcf4c/2795/path) at the top of the window to create a new **GPG** key.

<figure><img src="/files/FFitaxiH8wpHLXcWTQWL" alt=""><figcaption></figcaption></figure>

3. A new pop-up window will appear. Fill in the form and click on **create**.

<figure><img src="/files/fjdBXcAQyJu8BcMGN0qx" alt=""><figcaption></figcaption></figure>

#### Windows

1. Open [![](https://gpg4win.org/favicon.png)Gpg4win - Get Gpg4win](https://gpg4win.org/get-gpg4win.html)
2. Click on the **New Key Pair**

<figure><img src="/files/3ZGmUJjyKydMtEESaICC" alt=""><figcaption></figcaption></figure>

3. new popup window will appear. Fill in the form and click **OK**

<figure><img src="/files/gO7qt1Ve1XwdzEnWwQOw" alt=""><figcaption></figcaption></figure>

4. If the creation is successful, you will see a message similar to:

<figure><img src="/files/JutfSMb6u7tVTRKVMxsI" alt=""><figcaption></figcaption></figure>

### Exporting your public key

In order for ES to be able to encrypt the files we will need access to your public key. You can either share that key with us, or upload it to a key repository where we will be able to import it from.&#x20;

#### Mac

1. Open GPG Keychain. You should see a list with all your GPG keys:

<figure><img src="/files/0LunGgYKw3MF7cdDXEen" alt=""><figcaption></figcaption></figure>

2. Send the public key to the default key server (hkps\://keys.openpgp.org).

<figure><img src="/files/giBpZ5QpxSLAW5RVVzIq" alt=""><figcaption></figcaption></figure>

3. An confirmation email is sent - A link needs to be clicked:

![](/files/hUN00I75jvGLe1Y8aO8n)<br>

<figure><img src="/files/csc9PG9ju3NsbjbVHwT6" alt=""><figcaption></figcaption></figure>

### Windows

1. Open Kleopatra app:

<figure><img src="/files/xdH237LS5ZXpS7jteToc" alt=""><figcaption></figcaption></figure>

2. Change the key server to `hkps://keys.openpgp.org`:

<figure><img src="/files/rTjd12hCfMClQ81cgTX5" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/YauVnzwLb4P69Oc4Ll7G" alt=""><figcaption></figcaption></figure>

3. Publish your key to the key server (hkps\://keys.openpgp.org):

<figure><img src="/files/FWVmXschTl8nrMBg6ipK" alt=""><figcaption></figcaption></figure>

4. An confirmation email is sent - A link needs to be clicked:

<figure><img src="/files/qw5GeoPAU0d5q58NUdv1" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/kg5fW6tXP9CSo2PLe9c9" alt=""><figcaption></figcaption></figure>

#### Linux

1. Open your command line and run the following to upload your key to the key server:

   `gpg --keyserver keys.openpgp.org --send-keys <KeyID>`

   * You can see the **KeyID** by running:

     `gpg --list-secret-keys --keyid-format LONG`
   * In the output, identify the `sec` line, and copy the GPG key ID. It begins after the `/` character. In this example, the key ID is `30F2B65B9246B6CA`:

     `sec rsa4096/30F2B65B9246B6CA 2017-08-18 [SC] D5E4F29F3275DC0CDA8FFC8730F2B65B9246B6CA uid [ultimate] Mr. Robot <your_email> ssb rsa4096/B7ABC0813E4028C0 2017-08-18 [E]`
2. If you wish to export the public key as ASCII text, run this command, replacing `<KeyID>` with the GPG key ID from the previous step:

   `gpg --armor --export <KeyID>`

   * Copy the public key, including the `BEGIN PGP PUBLIC KEY BLOCK` and `END PGP PUBLIC KEY BLOCK` lines.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/vesper-insights/secure-data-file-transfer-guide/creating-a-pgp-key.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
