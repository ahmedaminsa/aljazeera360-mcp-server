> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/self-service-live-streaming/scheduling.md).

# Scheduling

To create a new event or tournament, click **Create New** from the top right of the main screen and follow the menu journey.

***

## **Creating a Tournament**

Tournaments group related events under a shared configuration. Setting up your Tournament correctly at the outset reduces the amount of configuration needed each time you create an individual event within it.

The creation flow is an 8-step wizard:

{% stepper %}
{% step %}

### **Tournament Details**

* Enter a **Tournament Name**
* Set the **Tournament Date** range — this should cover the full span of the tournament/competition, from first event to last
* Upload a **Poster** image — this will be used as fallback artwork when no stream is active
  {% endstep %}

{% step %}

### **Launch Configuration**

* Configure how and when infrastructure is launched and terminated for events in this Tournament
* This includes automation settings such as how far in advance of an event infrastructure should spin up
  {% endstep %}

{% step %}

### **Bitrate Ladder**

Select the bitrate ladder to be used for transcoding across events in this Tournament

* *A default ladder should have been established in advance for the realm (although there will be some exceptions)*
  {% endstep %}

{% step %}

### ***DRM Settings (optional)***

* Configure DRM rules if content protection is required
  {% endstep %}

{% step %}

### **Optional Settings**

* Additional tournament-level configuration
  {% endstep %}

{% step %}

### **Captions** *(optional)*

* Configure default caption settings for events in this Tournament
  {% endstep %}

{% step %}

### ***Geo Restrictions (optional)***

* Set geo-restriction rules to control where content can be viewed
  {% endstep %}

{% step %}

### **Review & Create**

* Review all settings before submitting
* Once satisfied, confirm to create the Tournament
  {% endstep %}
  {% endstepper %}

***

### **Creating a Live Event**

Each event must be created within an existing Tournament.

The creation flow is an 8-step wizard:

{% stepper %}
{% step %}

### **Select Tournament**

* Choose the Tournament this event belongs to
  {% endstep %}

{% step %}

### **Event Type**

* Either Standard or Third-Party Playback
  {% endstep %}

{% step %}

### **Event Details**

* Enter the event **Name**
* Set the **Start** and **End** times
* Add a **Description** *(optional)*
  {% endstep %}

{% step %}

### **Optional Settings**

* Additional event-level configuration, including poster image
  {% endstep %}

{% step %}

### ***Audio Settings (optional)***

* Configure audio tracks for the event
  {% endstep %}

{% step %}

### **Captions** *(optional)*

* Configure captions and translations
  {% endstep %}

{% step %}

### ***Geo Restrictions (optional)***

* Override or apply geo-restriction rules at the event level
* Can be used in conjunction with geo-templates <https://docs.onvesper.com/platform-knowledge-base/back-office/content/content-management/geo-templates-and-geo-policies-on-vesper-back-office>&#x20;
  {% endstep %}

{% step %}

### **Review & Create**

* Review all settings before submitting
* Once confirmed, events typically become available within 1–2 minutes
  {% endstep %}
  {% endstepper %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/self-service-live-streaming/scheduling.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
