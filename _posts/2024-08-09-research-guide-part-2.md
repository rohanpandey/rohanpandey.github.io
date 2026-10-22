---
layout: post
title: "Beginner Friendly Guide to Getting Started in Research (CS): Part 2"
date: 2024-08-09
tag: Research
description: "A step-by-step account of my literature review process: finding a topic, finding papers, and mapping the frontier."
original: https://docs.google.com/document/d/1QBtzJPE2ddEzLdCULxfatNVD9Oc7CuOdn7UER97eI10/edit
---

### Introduction

I wrote a post [\[Part-1\] Beginner Friendly Guide to Getting Started in CS Research]({{ '/blog/research-guide-part-1/' | relative_url }}) discussing a high level overview of the research process in CS (ofc. keeping out the parts where I doomscroll instagram lol). Given the surprisingly positive response, I now attempt to provide a detailed & transparent view of my process; a step by step account of how I do the drills, that are (hopefully) easy to follow along, replicate and eventually improve upon. 

**Disclaimer:** The details discussed here are a representation of my “ideal” process. I have to say that I often find myself skipping certain best practices.   
*\<[David Goggins’ voice](https://www.youtube.com/watch?v=OKN8dFO_ZLA)*\> Is this just because I’m not disciplined enough? *\</David\>*   
No (read: yes), but because PhD students like myself often have different commitments: multiple projects, reviewing, teaching, mentoring, fighting the monsters under our bed, you get the idea. 

### Get Started: Dive into the consumption phase (aka. Literature review)

This document focuses primarily on the “literature review” phase. I prefer the more informal term “consumption” phase; because I believe one should look beyond “reviewing”; to “consume” and end up at a place of understanding (and strong intuition) from where they can start building. 

The primary & unsurprisingly common question we tackle here, is *“How do I get myself up to speed on a topic?”*. What follows is a step-by-step description of how I try to understand the latest and greatest (not necessarily the same) of a particular topic. First, I will outline the main steps, after which we will dive into the details:

0. **Step 0 \- Finding a topic/area of interest:** In this section, I describe my view of how you can find interesting problems around you.   
   *TLDR:* know yourself (& what excites you) and look around.

1. **Step 1 \- Finding content/papers related to the interest area:** This section talks about how you should go around finding information pertaining to the topic you are interested in.   
   *TLDR: Search & dump.*

2. **Understanding how things work / connecting the dots:** After finding decently relevant pieces of information for the topic of interest, I describe how you should start connecting the dots to develop an intuition for the topic.   
   *TLDR: Read & organize.* 

3. **Diving deeper into what you like:** Once you know the basics, you do what most people are afraid to do: ask questions.   
   *TLDR: Be the fool, Be obsessed.* 

![Figure 1]({{ '/images/blog/research-guide-part-2/fig1.png' | relative_url }})  
Figure 1: High level overview of the consumption phase.
{: .caption}
#### Step 0:  Finding a topic or an area that is interesting

Before you start your dalliance with the mystic arts, an interesting question that often precedes is deciding your allegiance (slytherin or gryffindor). In other words, before you start diving into a topic, *how do you even find an area or topic within Computer Science that is “interesting”?*   
 

1. **Know Yourself:** I feel this is extremely underrated, especially as a beginner when you are either over or underconfident. You could use this framework to know where you fall, and by spending time observing, you should have a very broad idea of what topic(s) interest/excite you. 

   1. ***Know what inspires you:*** I have found that there are broadly two ways that people find their areas of interest:   
      1. **Top-down / Real world-Inspired approach:** I see this as taking inspiration from real world problems; finding things that bother you in the world and trying to fix them. I often find inspiration by observing problems this way (for me: it’s healthcare) – and then finding ways in which I can contribute. You could also think of this as a top-down approach, where you observe problems at the highest level of abstraction, and then work your way down to a level where you can provide solutions.   
            
      2. **Bottom-up / Tech-Inspired approach:** You could also be inspired to solve more technical problems. This could look something like trying to make a recommendation algorithm x% more accurate (i’m already addicted so please no lol), or solving an existing technical problem from a new perspective. A lot of my more theoretical friends fall in this category. This is a more bottom up approach, where you find a specific technical (CS) problem that bugs you and then try to fix it \- which in turn contributes to solving multiple problems up the ladder of abstraction.

      ***Note:*** These two approaches are not mutually exclusive, but just a broad lens that I like to use.

         

   2. ***Know where you are now:*** *What do you know and what do you not know?t?* You should know where you are with your current skill set, both technical and conceptual (at least broadly). This helps you manage your own expectations and helps to understand where you can start contributing now.   
        
2. **Look Around:** A good heuristic (in life) that I use, is to find people/groups who(se work) inspire me. For research, this looks like: Going up to university websites, looking at the different labs, and drawing inspiration from their work (read: themes and key ideas). There’s nothing dishonorable about seeking inspiration from people who are at the best of their games.   

**General Advice:** Do not wait to find the perfect problem (or solution), because it doesn’t exist\! Find a problem that is “good enough” and run with it. You can always decide to pursue different things later, but getting your hands dirty is 100% better than inaction. As a “perfectionist” myself, I (still) actively train myself to not devise the perfect plan and solve everything in my head, but to get going when I have enough to get started. 

![Figure 2]({{ '/images/blog/research-guide-part-2/fig2.png' | relative_url }})  
Figure 2: How do you find your starting point?
{: .caption}
#### Step 1: Finding papers that are relevant to my area of interest/problem

As talked about in the previous document, I find interesting research either when I’m, a) doing project/topic specific scoping, or b) through general consumption, i.e twitter, my lab slack, people I know etc. My key focus here is *on curating things I find interesting*.  

**Method A:** **Topic Specific Scoping**  
In practice, I use the following approach whenever I am trying to read up on a particular pre-identified topic:

1. **Search:** Go to Google Scholar or similar search engines (semantic scholar) for academic papers.   
   1. Search for review/survey papers on the topic. I search for the keywords of the topic \+ “review/survey paper” on Gscholar. **Note:** Review papers (if well written) are a great starting point that give a very detailed high level overview of the topic.   
   2. (Additionally) I search for the keywords of interest on Gscholar directly. Eg: “LLMs” \+ “Fairness”, “Language models” \+ “Fairness” \+ “Health” to find interesting papers. **Note:** I limit my search up to a certain page number on scholar search after which the relevance starts reducing (based on title).

2. **Dump:** I then create a list of these papers that I encounter; I use a combination of zotero and excel.  
   1. If I find a decent survey paper: I start generating a list of the recent articles that seem relevant and are cited in the survey paper. If the survey paper is recent enough, it should have the latest and OG work both cited. **Caveat:** Every field has its own pace, the definition of what is “recent” really depends on the topic/field you pick.  
   2. If searching with keywords: I only read the title and the abstract of the paper as my first filter, and dump anything I find interesting into an excel (or any other system).

      **Heuristic:** One heuristic that I implicitly use (not always) is that I will look at the i) citation count, ii) venue, and iii) authors as a signal for quality papers. (more in FAQ). 

At the end of this, you should have a list of papers that you found interesting which follow a common theme or are trying to tackle the problems you found interesting in step 0\. 

**Note:** It is indeed difficult to differentiate between good vs not so good research in the beginning, but trust me it gets easier over time. You will learn to see through (most, but not all) of the BS. 

**Method B: General Consumption**    
I also encounter a lot of interesting papers on social media (twitter) or my lab’s slack, that I end up bookmarking/saving. 

1. **Bookmark:** I let them simmer in my bookmarks for a while, a lot of them don’t end up being read; and that is ok\!.   
2. **Dump:** I have a section in my zotero called “interesting ideas” where almost all papers that seem interesting end up, and are read later.  

![Figure 3]({{ '/images/blog/research-guide-part-2/fig3.png' | relative_url }})  
Figure 3: Finding content that is relevant to your interests.
{: .caption}
#### Step 2: Understanding where the frontier of research is, i.e how is it all connected

Having done some homework and curated your reading list. The next thing you want to ask yourself is, *“how do I go from a list of related literature to a broad understanding of (the latest work in) this topic”*. Answer? Reading and structuring.  

I follow a simple templatic approach to do this, which allows me to get through my (sometimes not so easy) readings from the list curated above:

1. **Read:**   
   1. (If available) Read the review paper first.  
   2. Then, sort the list of interesting papers in reverse chronological order, filter the papers based on title and abstract, (or pick an OG paper), and start reading. **Note:** refer to FAQ on “how to read a paper” and “signals for filtering quality papers”.   
2. **Organize:**   
   1. While reading, I start filling my literature review sheet (fill out the important details in an excel) [\[Template\] Literature Review](https://docs.google.com/spreadsheets/d/1nCJ74cQuNaGy9HESXNfoZMk8_gXtpsUdz_Dgbs4hZ_E/edit#gid=0)**.**   
      **Important:** My objective when doing this is not to understand everything 100%, but to understand the topic, landscape and current views on the topic. Limiting myself to just filling this sheet (as best I can) allows me to let go of *“perfection”* and focus on my objective. This is very underrated imo, it helps me keep going when learning complex topics, which get easier to understand only over time.   
   2. **(Optional)** Create a separate document for each topic – write down whatever you learn about the topic from your readings that you think is useful / might need to refer later. Try to prove to yourself why certain things make sense. 

![Figure 4]({{ '/images/blog/research-guide-part-2/fig4.png' | relative_url }})  
Figure 4: Start connecting the dots by reading and organizing what you read.
{: .caption}
#### Step 3: Dive Deeper

Once you have completed a broad overview of the topic, you should have a high level intuition of what is happening and recognize the “vibes”. The next step is to shift your focus to diving depth first. It’s repeating what we’ve already done but with different objectives in mind: 

1. Read fewer papers, but get into more details:   
   1. Based on your previous reading and organization, you will have a fairly good idea of the nice vs not-so-nice papers.   
   2. Read the important papers and ask yourself more questions about what we know/what is interesting and try to document your thoughts\!   
      **Note:** A distinguishing factor between people I find cool in research vs not, are people who question everything (even the assumptions that most people take for granted). Be the fool\! Ask questions\!   
2. Learn as you go: As you go deeper and encounter newer concepts \- read them as required (you cannot know everything beforehand). **Advice:** One mistake I made in the past was to try to know “everything” before moving forward (be it reading concepts, documentations, etc). Over time, I have realized that it’s important to know just enough and keep moving forward. It gets easier only with practice.  This does not mean skip the basics tho\!

#### FAQs

1. How to use the quality signals mentioned for filtering papers?

   I use a combination of the following as a filter (mostly implicitly) while figuring out what is worth my time when reading papers:  
1. **Citation Count:** This is a count of the number of times this particular paper has been cited by others. In an ideal world, a paper that is “important” should be cited and used by other works as inspiration. **Caveat:** People have found a way to rig this; salami slicing (split a simple work into multiple papers) and citation rings (people collectively decide to cite each other's papers) are a few examples of that.  
2. **Venue:** Certain venues are more selective than others, a knowledge of which venues are considered “top-tier” is also a good heuristic. **Caveat:** Even peer review is broken (more on that later), but it’s the best system we have.

     
   There are preprint servers like arXiv and biorxiv which allow authors to put work that has not undergone peer review on the internet, while reading such papers always be skeptical (also be skeptical about peer-reviewed work, too). 

   (Not so exhaustive & a very lazy) representation of venues that I like are below:

   1. Conferences: ICLR, ICML, NeurIPS, ACL, NAACL, \*ACL, EMNLP,....  
   2. Journals: Nature, JAMA, .. (I work in healthcare and ML)

2. How to read a paper?  
     
   As with anything, I would approach this based on objectives. Almost always, I do not want to spend 4 hours trying to understand everything for every paper I read. Before I begin reading, I ask myself what my objective is wrt to the paper, and based on that I usually do the following:  
   1. **If the topic is new:** I will read through the abstract, introduction and related works. This will hopefully give me a good intro to the topic.   
   2. **If I am aware of the topic:** I will read through the abstract, conclusion and skim through the methods to understand the concept broadly.  
   3. **If I know the topics well / the paper really intrigues me:** I will read it more thoroughly i.e go through the methods in more detail and try to work out a strong intuition for the proposed technique. 

3. What if I don’t understand something?  
     
   This happens more often than people would like to accept. It really depends on where you are in your research journey,   
1. **If you’re just starting out:** Be comfortable with not knowing a lot of the details. As long as you feel like you’re making progress \- keep going. **Note:** This does not mean ignore the basics, but it means be comfortable not knowing.   
2. **If you’re deep into a topic/ you’re working on a project,** you should:   
   1. Talk to a mentor who’s worked in that area for a while (if you’re able\!)  
   2. If not, refer to more “classical” papers, textbooks, tutorials, and reach out to public communities on discord servers.  
      **Controversial advice:** Learn to say “I don’t know”, and you’ll see that you’ll learn things faster and people will respect you more. 

4. You seem to prefer doing a lot of things in sheets over docs, why?  
     
   Having a table structure gives me a good overview of different papers. I find writing in docs useful too, but having everything in one view helps me connect ideas, thoughts etc. It probably also has something to do with my background in consulting, where we looove spreadsheets, for good reason, lol. I think there is a lot of value in structuring and documenting things, it is less common in research than you’d imagine.  
     
5. How do I know if I know enough or should I keep reading/learning?   
     
   At the risk of sounding redundant, whenever I do something, I try to ask myself, *what is my intent behind this?* When I’m doing a consumption phase or literature review for a new topic, my primary intent is to develop a very high level intuition of the topic (the main idea, usage, pros, cons). If I want to go deeper, I spend more time diving into the nuts and bolts of the topic (read: math and code), the trajectory of the topic (where did it start and where we are now), and the latest cool ideas. It really depends on what your objective is.

6. If I’m just getting started, should I go for what’s hot vs what interests me?  
     
   **Broadly:** I strongly believe that there is enough space to do meaningful work in almost all areas. Of course, some areas have more space, visibility, and ease of entry than others, but in the long term you should ideally work on your interests, while making the least amount of sacrifices to the high power, that I call “hype”; people use different names.   
   **Caveat:** You should always think about where you are in life, if you are looking for jobs/have bills to pay/people to care for \- you should be primarily spending time optimizing for what gets you a job/more money vs exploring your interests. It’s about priorities. 

7. What do you mean by an “interesting” research area?  
     
   The good (and bad) thing is that the definition of “interesting” is and should be subjective; it evolves over time, at both, an individual and community level. I think one should consider their personal interest first (which allows one to persist when things don’t work \- 99% of the times), and be in touch with reality, in the sense that their interest area should have overlap with what is useful to the broader scientific community (you don’t want to be out there chasing unicorns). 

### Acknowledgement

This document evolved out of this Miro board ([https\://miro.com/app/board/uXjVNEw4LMY=/](https://miro.com/app/board/uXjVNEw4LMY=/)) which I started using for a few intro sessions with people. I would like to thank Casey Maloney for detailed comments and suggestions on an early draft of this document. I would also like to thank Utkarsh Sharma and Kartikeya Chaturvedi for their suggestions.

This document would definitely have elements from other advice/content available, if there’s anything that I have inadvertently copied \- please let me know. PS: All opinions are my own.
