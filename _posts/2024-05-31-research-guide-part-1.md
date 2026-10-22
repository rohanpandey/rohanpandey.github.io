---
layout: post
title: "Beginner Friendly Guide to Getting Started in Research (CS): Part 1"
date: 2024-05-31
tag: Research
description: "A first-principles take on what CS research looks like day to day, whether it's for you, and how to sign up."
original: https://docs.google.com/document/d/16JEHbP9MqkjLld1pD2DJ5xEf0Lx6cTaZ-6WUqnpvWVY/edit
---

### About me

I am a PhD student at the CS department at the University of Massachusetts Amherst. My primary research interest is making robust and trustworthy language models work in the wild, especially in healthcare settings. Broadly, I care about democratizing access to healthcare and improving healthcare outcomes across the world, and I believe that technology can help us get one step closer.

To begin contributing to scientific research, I had to learn how to leverage limited resources and mentorship. This is a document for my past self, a reflection, that provides a systematic approach to answering the questions: “What is research? Is it for me? and how do I sign up?”.This document takes a first-principles approach to understanding the science of conducting  well-grounded research, and hopefully has something for everyone.

### Introduction

This is starting as pieces of advice intended to lower the barrier of entry in computer science research. The prerequisites are pretty strict: curiosity and some free time after school (insert sarcasm sign here). It is perfectly ok \- if you do not have any prior experience in research, in fact, a fresh perspective might even be better. (If you ask me, we need more unconventional ideas that move beyond passing the “benchmarks” in CS research.)

**Note:** This is not supposed to be a learn how to code guide. There are existing resources that have already done a better job than I ever could. However, if there is enough interest, I would be happy to compile my thoughts on how I approach “writing code” in CS research — general or for machine learning. 

Based on my initial thoughts, I am going to cover a few ideas that are worth articulating (more selfishly to just get them out of my head) and are topics that people often ask me. The current list of topics that I will cover are:

1. **Overview of research:** An introduction to what doing CS research (with a focus on empirical ML research) looks like from a high-level perspective. I will discuss the components as well as their significance.   
2. **Layman’s guide to doing research:** A step-by-step guide on how I start doing research from scratch. This would incorporate strategies that I use (or have used) and have worked well for me.   
   1. Part 2: Consumption Phase has been published\! [\[Part-2\] Beginner Friendly Guide to Getting Started in CS Research]({{ '/blog/research-guide-part-2/' | relative_url }})  
3. **Fascinating areas:** A list of running topics and areas that I find interesting, hopefully also with more specific research questions (in the spirit of open science), in case you would like to collaborate with me or are looking for inspiration. 

### A “slightly” naive view of doing research: What does CS research look like on a daily basis

When I ask people what they think of computer scientists, I hear one of two responses: either a person sitting behind a computer screen (best imagined with a slouched back) writing code or someone staring at a whiteboard (again, best imagined with frizzled hair) scratching their head in agony. In my (limited) experience, I think research has less to do with physical attributes, although I do admit that some stereotypes are not that far off.  Research is a set of basic drills on repeat (read: perseverance), interspersed with moments of glimmer and glum. What does this look like? A LOT of reading, writing ideas & code, running systematic experiments, collaborating with brilliant minds (the best part imo), and above all hoping that you come up with something meaningful to share with the rest of the world. 

For ease of explanation and to give you a glimpse into the life of a CS researcher, I have broken down the process into various stages. **Note:** These stages are not mutually exclusive or exhaustive. In reality, there is a lot of back and forth that takes place, but this simplistic view will give you a quick insight into the game of research. 

#### Level 0: High-Level Overview

If I think about the components of research at the highest level of abstraction that are easy to understand, I would break it down into the following components. (If you want to avoid the storytelling, skip to the diagram directly\!)

1. **Consumption phase:** It all starts with a dire thirst for knowledge (or advisor's orders) that makes you spend countless hours trying to find the fountain of knowledge (one interesting research idea). In other words, you usually start with consuming, i.e trying to read up as much as possible on a particular topic/field, to understand what is already known by the scientific world. The purpose of this phase is two fold, i) improving your understanding of that area/topic and ii) eventually creating a new piece of knowledge. 

2. **Ideation phase:** With the new found wisdom that comes from drinking the elixir at the fountain of knowledge, you now seek to find the most important problem that could use your great powers. In practice, after consumption, you spend time coming up with an interesting idea or question that is useful for the community (unexplored, underexplored, has significant impact, etc).

3. **Experimentation phase:** Now that you know you want to solve world hunger, you want to test your brilliant idea in the hope of seeing the world change right before your eyes (and you should probably take a camera because you’d want to record it). Realistically, this is the phase where you design your experiments and try to produce evidence to prove/disprove your idea. **Remember:** falsifying your hypothesis is also a great result\! 

4. **Presentation phase:** Now is your time to shine, your spotlight, where you get all the glory and ofc a red carpet. The reality is a bit less glamorous, usually one spends time trying to package their results so they reach the people who would appreciate and make good use of the findings (a paper). 

![Figure 1]({{ '/images/blog/research-guide-part-1/fig1.png' | relative_url }})

Figure 1: High-level overview of the research phases.
{: .caption}
#### Level 1: What does each phase look like?

1. **Consumption Phase:** The consumption phase is really when you try to understand what others know and care about. This serves as your knowledge base for a particular topic or field. For me, it looks like this:  
   1. **Finding content:** Information relevant to you can be from multiple sources (papers, lectures, tutorials), and typically it's either:  
      1. **Project-driven:** where you already know what topic you want to work on and you want to survey what is currently known.  
      2. **General consumption:** where you come across papers in conferences, and social media, that you find interesting and want to learn more about.   
   2. **Curation:** This usually goes hand in hand with finding content, it involves curating the interesting papers (making a pile of papers).   
   3. **Filtration:** After having a list of papers, you need to filter out which papers are “important”.   
   4. **Read:** Now it’s time you read the selected list of papers. Depending on your goal, you can decide to either quickly skim through or deep dive. 

![Figure 2]({{ '/images/blog/research-guide-part-1/fig2.png' | relative_url }})  
Figure 2: Overview of consumption phase.
{: .caption}
2. **Ideation Phase:** Now that you have read a bunch of stuff, next comes the more fun part (at least for me). After understanding what other people know, you attempt to come up with new ideas.  
   1. **Listing interesting ideas:** This usually involves effort in trying to identify gaps in current work, future work that others have suggested (usually found in the discussion), trying combinations of multiple ideas, etc.   
   2. **Prioritizing ideas:** Based on factors such as relevance to community, ease of implementation, and personal interest \- try to pick ideas that check most of your boxes.  
   3. **Refinement:** Once you have a broad idea or question that you want to pursue, you want to spend some time refining it. I usually try to come up with a specific research question, write multiple hypotheses and place bets on what would work (fun to look at retrospectively).

![Figure 3]({{ '/images/blog/research-guide-part-1/fig3.png' | relative_url }})

Figure 3: Overview of Ideation phase.
{: .caption}
3. **Experimentation Phase:** Now that you have a “good-enough” research question (which is good enough to get started), or idea that you want to pursue, you wanna get your hands dirty.  
   1. **Experimental Design:** First, given you have a research question and a set of hypotheses, you want to design your study in order to prove/disprove each of your hypotheses. This involves deciding on datasets, experiments, models, metrics etc.  
   2. **Writing Code:** Then you write the code, run the experiments and collect metrics that help you get closer to the truth.  
   3. **Decipher**: Once you get the metrics accumulated, you can start interpreting what those metrics mean and hopefully have something interesting. 

![Figure 4]({{ '/images/blog/research-guide-part-1/fig4.png' | relative_url }})

Figure 4: Overview of experimentation phase.
{: .caption}
4. **Presentation Phase:** So now that you have solved the most important problem in this world, you want to share your success. This usually is the following:  
   1. **Structure:** Start with creating a structure for the manuscript; write up the heading, titles, and main punchlines.   
   2. **Dump and Refine:** Input the main results, followed by the other sections and refine with your collaborators.   
   3. **Submission:** Lastly, submit it wherever you'd like\!

![Figure 5]({{ '/images/blog/research-guide-part-1/fig5.png' | relative_url }})  
Figure 5: Overview of presentation phase
{: .caption}
### FAQs

1. Is there any point where you have a full grasp on the prior knowledge of a subject?

   The more time I have spent in research, the more I realize how little I know. Don’t get me wrong, I definitely do understand things at a wider and deeper level as I spend more time, but I am also constantly humbled as I realize that I cannot know it all. For a field like deep learning/LLMs, a lot is still unknown and works on intuition. From a practical perspective (in a world where you need to publish papers), I like the approach of trying to get “just enough” intuition and knowledge of a topic so that i) I do not reinvent the wheel, and ii) I can build knowledge on top. It is very easy to go down the rabbit hole of trying to know everything before starting \- but that is near impossible.   
     
2. How do you organize what you've learned? or do you just read and think about it?  
   1. For papers: I like to keep a mix of 1\) papers that I find interesting and want to annotate and read later in zotero, and 2\) when doing specific searches for a project, I do that in excel with the objective of doing a literature review. (more details in next blog).  
   2. For topic specific knowledge: I usually like to maintain topic specific docs where I write down all I learn / read for a particular topic \- helps me refer to it later. 

3. How much time does all of this take?   
     
   This really depends on the nature of the project, how exploratory vs pre-decided it is. In my experience, I have had projects that have roughly taken from 6months to 2.5 years, from start to publication. What does this mean? This means that you need to have patience when doing research, often ideas and problem statements evolve, being flexible and having patience are virtuous traits for doing quality research.  
     
4. How much should I hedge my bets? Should I pursue multiple different projects or focus on one topic at a time?  
     
   I would suggest as a beginner (even later) you should focus on one thing at a time. It is often enticing to put yourself in multiple projects in the hope that one of them works. Believe me, there is more value (in the long term) in learning from failures from a single project where you go in depth, than papers from projects where you barely scratched the surface. 

### Acknowledgement

This document evolved out of this Miro board ([https\://miro.com/app/board/uXjVNEw4LMY=/](https://miro.com/app/board/uXjVNEw4LMY=/)) which I started using for a few intro sessions with people. I would like to thank Casey Maloney and Tiye Ngachoko for their comments and suggestions on an early draft of this document. 

This document would definitely have elements from other advice/content available, if there’s anything that I have inadvertently copied \- please let me know. PS: All opinions are my own.
