# Message Notification Router

Build an AI-powered system for WhatsApp that decides which messages deserve immediate attention, which should wait, and which should be muted.

The system must reason over **multimodal messages**, including text messages, image posters/screenshots, and voice notes.

WhatsApp is noisy. A user can receive family chats, society notices, school updates, co-worker messages, business account promotions, image posters, voice notes, and scams in the same message stream. Treating every message the same creates two bad outcomes: important messages get missed, and unwanted or risky messages interrupt the user.

Your task is to build a **message notification router** for this platform. For every incoming WhatsApp message, the system must decide whether the user should be interrupted now, whether the message can be batched into a digest, or whether it should be muted.

The routing decision must be personalized to the receiving user. A sale poster may be useful for one user and unwanted noise for another. A payment reminder may be legitimate from a trusted admin but risky from a new sender. A muted family group can still contain an urgent direct mention. At the same time, clear scam or safety risk should be muted regardless of the user's usual engagement.

## What You Need to Build

Build a system that reviews each incoming message and decides how it should be handled for that user:

- `notify`: important enough to interrupt now
- `digest`: useful, but can be shown later
- `mute`: low-value, repetitive, unwanted, suspicious, or unsafe

Your system should use the provided message, user, group, business, media, and historical interaction data to make personalized routing decisions.

## Files provided

All participant-facing files are inside `dataset/`.

Only `dataset/messages.csv` needs predictions. The other files provide context:

1. `dataset/messages.csv` - Incoming messages that your system must route.
2. `dataset/sample_messages.csv` - Example messages with the expected `action`, `message_type`, `reason`, `confidence`, and `evidence_message_ids` columns filled in. Use this only to understand the expected output format and style.
3. `dataset/users.csv` - Basic user notification behavior, such as quiet hours and recent opens, replies, dismissals, and reports.
4. `dataset/groups.csv` - Basic information about each group chat, such as group type, size, admins, and recent activity.
5. `dataset/group_members.csv` - How each user relates to each group: role, activity, read/reply behavior, dismissals, and mute state.
6. `dataset/business_accounts.csv` - Information about business senders, including brand identity, verification, domain used by the sender, account age, and reports.
7. `dataset/user_business_history.csv` - Whether a user has a recent relationship with a business, such as orders, bookings, payments, opt-ins, or opt-outs.
8. `dataset/message_history.csv` - Past messages received by users. These help identify repeated patterns, ignored messages, useful updates, and risky content.
9. `dataset/message_events.csv` - How users reacted to those past messages: opened, replied, dismissed, muted, or reported.
10. `dataset/images.csv` - Image IDs and file paths for image messages.
11. `dataset/voice_notes.csv` - Voice note IDs and file paths for audio messages.
12. `dataset/daily_notification_summary.csv`  - Daily notification load for each user.
13. `dataset/output.csv` - Blank submission template. Fill this file with your predictions.

Media files referenced by `images.csv` and `voice_notes.csv` are available under `dataset/media/`.

## Input schema

Each row in `dataset/messages.csv` represents one incoming message.

Input fields:

- `message_id`: unique incoming message ID
- `user_id`: user receiving the message
- `conversation_type`: `personal`, `group`, or `business`
- `group_id`: group ID if the message is from a group
- `business_id`: business ID if the message is from a business account
- `sender_user_id`: sender user ID if the message is from a user
- `created_at`: message timestamp
- `message_text`: text content for text messages; empty for voice-note messages
- `media_type`: empty, `image`, or `voice`
- `media_id`: linked image or voice-note ID, if present
- `forwarded_count`: forwarding signal



## Required output

For every row in `dataset/messages.csv`, generate one row in `output.csv`.

Required columns, in order:

- `message_id`
- `action`
- `message_type`
- `reason`
- `confidence`
- `evidence_message_ids`



## Output meaning

- `action`: final routing decision
- `message_type`: best-fit message category
- `reason`: short human-readable explanation for the decision
- `confidence`: number from `0` to `1`
- `evidence_message_ids`: semicolon-separated historical message IDs used as evidence; write `none` if no useful historical message exists



## Allowed values

`action`:

- `notify`: interrupt the user now
- `digest`: safe but low priority; show later
- `mute`: repetitive, unwanted, low-value, suspicious, scam-like, or unsafe for this user

`message_type`:

- `personal`
- `urgent`
- `event`
- `payment`
- `business_update`
- `promotion`
- `greeting`
- `forward`
- `spam`
- `scam`
- `unknown`



## Important Behavior

Your system should make personalized decisions using the full context provided. Similar-looking messages may need different actions depending on the user, sender, conversation, business relationship, and media content.

The final decision should balance usefulness, urgency, repetition, and risk. Risky messages should use `mute` with an appropriate `message_type` such as `scam` or `spam`.

## Evaluation

Your `output.csv` will be compared against hidden ground-truth labels.

The scoring will consider:

- correctness of `action`
- correctness of `message_type`
- usefulness and consistency of `reason`
- whether `evidence_message_ids` point to relevant historical messages
- reasonable confidence calibration

## Submission

Submit:


| File              | Description                                                          |
| ----------------- | -------------------------------------------------------------------- |
| `code.zip`        | Full runnable solution, prompts/configs, and README                  |
| `output.csv`      | Predictions for all rows in `dataset/messages.csv`                   |
| `chat_transcript` | Conversation transcript showing how you developed or used the system |


These are the must-haves. Beyond that, participants are encouraged to improve retrieval, prompting, evidence selection, confidence handling, batching, caching, or safety logic.
