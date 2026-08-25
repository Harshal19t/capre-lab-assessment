# Improving the Notion → CRM handoff

## How it works today

Once a week, someone will filter Notion to see which leads are ripe, will export them to a spreadsheet file, and then paste them in an existing Excel document. The Excel file takes care of some automatic cleanup separating the first and last names, fixing the website URL. Then, someone needs to manually log into our CRM system, Attio, and look for each individual lead, determine if it is an entirely new business or not, enter all information, and finally log back into Notion to mark this lead as done. So the actual "moving the data over" part is fully manual, and so is the "is this a duplicate" decision that all lives in one person's head, every single week.

## What I looked at in this week's list

After working through the leads, there are several observations on how manual
work is necessary and cannot be done automatically:

- **One of the companies is represented twice** as it consists of two people
  from the same company, both on the list. Without careful consideration,
  two of the same companies will be created, each having one person in
  CRM.
- **One of the leads does not have an email address** but has a LinkedIn
  profile instead. This lead definitely requires manual work.
- **Several leads appear to have been previously contacted** the notes
  mentioned that the lead reached out before under a different email or was
  considered in a previous campaign. None of the tools used today can check
  if this is true.
- **Minor inconsistencies in formatting** such as website links and company
  sizes being entered in slightly different ways. Minor detail but it still
  adds to the mess in CRM.

## The approach I'd take

Automate a small step between Notion and the CRM that takes care of
the tedious part itself:

1. **Take leads straight from Notion** without the need to export a file
   and paste it anywhere else.
2. **Data cleaning** as it is done in the spreadsheet but more reliably
   and consistently—fixing website formatting and company size formatting.
3. **Search CRM before making an addition.** In the process of automation,
   the system will check whether this person or company is in the CRM
   already and update the information in case if it is present there. It
   will treat the companies as a single organization in case they are the
   same but associated with other people who are in this list of leads.
4. **Ignore the uncertain cases.** Cases when no email address was found
   and when the notes indicate that the person might be already in the CRM
   with some other information won’t be processed automatically. As well as
   it happens now, such leads should remain untouched.
5. **Mark the entry as closed.** When the lead has been successfully
   added to the CRM, the task should be marked as completed automatically
   in Notion.

What is the purpose of using this method? It reduces manual typing and manual searching as much as possible, but still leaves room for human judgment in the one area where it actually matters – determining whether or not an item already exists in some cases.

## What I'm assuming, and what I'd confirm before building this for real

- The team having access to the Notion and CRM APIs
  This has not been verified by me, but rather an assumption
- When two contacts of the same company appear in one batch, it means that they
  will have one company record associated with two contacts, not two different
  company records. It is my interpretation based on this week's data, but I
  have not verified this information with Maya - I would start with that because
  it affects automation behavior.
- I did review the video recording of what Maya does. There's no sound, but it is a
  silent recording of the screen. It supports the description above: she extracts the filtered
  records from Notion, pastes them into the Excel file and processes it in the exact
  same way as described on the "Start Here" tab of the Excel file.

## What I'd do with more time

- Test out whether the check-the-CRM-first step will reliably match up with
  reality or whether you'll just have to assume that it will be perfect
  somehow.
- Create a fast way for the individual to approve the small number of
  leads that need a human eye each week through some form of chat message
  instead of opening up a spreadsheet.
- Look into whether there is a current solution that connects Notion to this
  particular CRM already to avoid doing unnecessary work.