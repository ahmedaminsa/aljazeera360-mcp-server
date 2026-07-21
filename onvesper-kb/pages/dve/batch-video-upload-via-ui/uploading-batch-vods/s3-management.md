> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/dve/batch-video-upload-via-ui/uploading-batch-vods/s3-management.md).

# S3 management

Amazon S3 bucket access is typically controlled through AWS Identity and Access Management (IAM) credentials.

## How to create a new S3 bucket

1. Go to the [AWS Console](https://aws.amazon.com/) and sign in with your AWS account credentials.
2. Under the "Storage" category go to S3
3. **Create a new bucket:**
   * Click on the "Create bucket" button.
   * Enter a unique name for your bucket.
   * Select the AWS region for your bucket. Choose a region that is geographically closest to your users to reduce latency.
   * Click "Next."
4. **Configure options:**
   * You can configure additional settings for your bucket, such as versioning, logging, and tags. You can leave these as default for now or configure them based on your requirements.
   * Click "Next."
5. **Set permissions:**
   * Configure the permissions for your bucket. You can choose to block all public access or set more granular access controls.
   * Click "Next."
6. **Review and create:**
   * Review your configuration settings and if you're happy click "Create bucket."
   * Create a IAM user / AWS user and grant the write access to the S3 bucket

## How to find your IAM credentials

To interact with an S3 bucket, you need AWS access key ID and secret access key associated with an IAM user that has the necessary permissions.

Finding Existing IAM User Credentials:

1. **IAM Console:**
   * Log in to the AWS Management Console.
   * Navigate to the IAM service.
2. **Locate IAM User:**
   * In the IAM console, click on "Users" in the left navigation pane.
   * Find the IAM user associated with your S3 bucket.
3. **Access Keys:**
   * Select the IAM user, and go to the "Security credentials" tab.
   * Under the "Access keys" section, you can view the existing access key ID. If there's no existing access key or you want to rotate it, you can create a new one.
4. **Create New Access Key (if needed):**
   * If you need to create a new access key, click on the "Create access key" button.
   * Save the new access key ID and secret access key. Remember that the secret access key is only shown once, so make sure to download it or save it in a secure place.

{% hint style="info" %}
Once you have created your S3 bucket, please share the below in a secure manner (password-protected zip via email, perhaps) with your client account management team:

* Bucket Name
* S3 Region
* Access Key ID
* Secret Access Key
  {% endhint %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/dve/batch-video-upload-via-ui/uploading-batch-vods/s3-management.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
