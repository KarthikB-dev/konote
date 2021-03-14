# konote
This project has not yet been completed and so has very limited functionality as of now.


## What is konote in one sentence?
A notetaking application that helps you organize a great deal of notes, and that helps you apply 
[evidence based study tips](https://www.youtube.com/watch?v=ukLnPbIffxE) like active recall and spaced repetition.


## Why the name _konote_?
This application will deal a _knockout blow_ to your laziness and poor work ethic!
And it helps you take notes.


## I'm interested. Tell me more!
konote has two main functions. The first is to help you organize information as you read it
by organizing notes in a tree structure, where chapters 'branch' off a book, chapter sections
'branch' off a chapter, and individual topics 'branch' off chapter sections. This will give 
you a higher level view of the topic. It's expected that you won't retain all the information 
on your first pass through the chapter, which bring us to applying active recall. Within this 
tree structure of notes, you will create practice questions for yourself. This is accomplished
by creating a directory for a question, and storing the answer as a [hidden file](https://www.wikiwand.com/en/Hidden_file_and_hidden_directory)
within that question directory. When you return to your notes to study, konote will use the 
```tree``` command to display your notes. Because the answers to each practice question are 
stored in hidden files, they won't be revealed until you choose to view them
using the command ```tree -a```. This part of the studying process is where most of the learning
happens. 


Konote determines what topics require revision by taking input on how comfortable you were 
with the chapter or chapter section. It asks for a score from 1-5, with 1 meaning very poor 
or limited understanding of the topic, and 5 meaning mastery. This is then stored in the directory
description(which is stored in ```description.txt```), which stores other information, like whether 
the directory is a collection of books, chapters, or chapter sections. Note that a given directory
only allows you to create subdirectories of matching types. You aren't allowed to make new books
in a chapter for example.
