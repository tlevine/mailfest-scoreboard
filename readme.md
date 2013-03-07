Mailfest Scoreboard
======

**Mailfest** is a hypothetical email-writing event. People meet with food and
alcohol to write emails that they've been meaning to write in company of other
nice people. The company of others also helps them deal with difficult emails.

* People can work together on the composition of individual emails.
* People might discuss problems with email and create small tools to help with
    email composition.
* People can ask for help on a particular sort of email.

The **Mailfest Scoreboard** keeps track of how much has been accomplished.
Once it has been installed, mailfest participants just need to BCC all emails
that they write during the mailfest to the email address for which the
scoreboard has been configured. The scoreboard will produce statistics about
the emails that have been sent and about the people who have been sending them.

The emails are deleted immediately after they are read, and information about
recipients is deleted, but you should still avoid sending particularly secret
things to the mailfest scoreboard.

## Install
Specify the IMAP server credentials, and then run `./scoreboard`.

## Statistics
The following features are extracted from each email.

* `From` field
* Date
* Size of email, ignoring attachments
* Size of the `Subject`
* Number of attachments
* Number of recipients in the `To` field
* Number of recipients in the `Cc` field
* Whether the title starts with "Re:"
* Whether the title starts with "Fwd:"
* Whether it was sent from a Google Mail server

Whenever "size" is mentioned, both of the following metrics are collected.

* Number of characters
* Number of words

To be clear: The name and email address of the person who sent the email
will be recorded so that we can report things like the number of emails that
each person sent. Aside from this feature, the features shouldn't be able to
reveal much private information.
