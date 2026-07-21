> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/users-1/managing-a-user-account/make-revoke-universal-user.md).

# Make/Revoke a Universal User

### MAKE A UNIVERSAL USER <a href="#make-a-universal-user" id="make-a-universal-user"></a>

If a customer needs to access the site that is outside of allowed VPN, then you can make a user a Global/Universal user which means they can bypass any VPN proxy in place. To make a customer Global/Universal user, you need to go to the ‘Customers’ section in Back Office, search for the customer via Username, Card Number, Name or EXID.

<figure><img src="/files/sbd5AZtz9xqoHusKZ2ux" alt=""><figcaption></figcaption></figure>

Click on the customer’s name and you will be taken through you to the account page. Click the ‘Actions’ button and select ‘Make Universal’ from the drop-down menu.

<figure><img src="/files/tH0nXiKVutsbVdIt3Bxk" alt=""><figcaption></figcaption></figure>

In the right-hand side corner of the screen, you will notice a notification will pop up that will confirm that the customer has been made a Universal User.

When you exit the customer’s account, you can re-search for the customer and you will notice that next to the customer’s email/ID it will show the Universal icon.

<figure><img src="/files/HxFXkcLzp0HHD2ZMnImg" alt=""><figcaption></figcaption></figure>

The customer can now access everything on the platform and not be held up by geo-restrictions that may be in place for other customers who would need to use a VPN to access certain content.

### REVOKE A UNIVERSAL USER <a href="#revoke-a-universal-user" id="revoke-a-universal-user"></a>

If you need to remove a customer’s Universal user status then this is easy to do, you just need to follow steps above however when it comes to the ‘*User Actions*’ button, instead select the ‘*Remove Universal*’ option.

<figure><img src="/files/PwiF53W6L3JjyaV0OALv" alt=""><figcaption></figcaption></figure>

In the right-hand side corner of the screen, a notification will pop up that will confirm that the customer status has been changed. When you exit the customer’s account, you can re-search for the customer and you will notice that the customer’s email/ID will now show without the Universal icon. The customer will now be geo-restricted and will need to use a VPN if they are watching content that is unavailable for the territory that they are in.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/users-1/managing-a-user-account/make-revoke-universal-user.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
