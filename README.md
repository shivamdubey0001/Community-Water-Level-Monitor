# 🌊 Community Water Level Monitor

> **"Track water levels, stay ahead of floods!"**

Hey! This is a simple tool I built to help people track water levels in their area. You know how during monsoon season, water levels can get dangerous really fast? This tool helps you keep an eye on that.

---

## 🤔 Why I Made This?

Living in India, we all know how unpredictable water levels can be. One day it's normal, next day your street is flooded! I thought - what if there was a simple way to track this data over time? Something that even my grandmother could use from her phone or computer.

So here we are! A tool that:
- Records water readings (just type in the numbers)
- Shows you graphs so you can see trends
- Alerts you when water gets too high
- Creates simple reports you can share with others

---

## 📱 How Does It Work?

Think of it like maintaining a diary, but for water levels! You just tell the program:
- Which city/area you're in
- What's the current water level
- And it remembers everything for you

## 🎯 Perfect For:
- Village committees tracking river levels
- Housing societies monitoring drainage
- Students working on environmental projects
- Anyone who wants to understand water patterns in their area

---

## 💻 Quick Start Guide

### Step 1: Add Your First Reading
```bash
python main.py add --city "Mumbai" --level 1.5
```
*Just recorded 1.5 meters of water level in Mumbai!*

### Step 2: See All Your Data
```bash
python main.py list
```
*Shows you everything you've recorded so far*

### Step 3: Make a Graph
```bash
python main.py graph --days 7
```
*Creates a nice graph showing last 7 days of data*

### Step 4: Generate Report
```bash
python main.py report
```
*Creates a text file with all your data - easy to share!*

### Step 5: Set Safety Alert
```bash
python main.py threshold --set 2.0
```
*Now it'll warn you if water goes above 2 meters*

---

## 🖼️ What the Graph Looks Like

The tool creates beautiful graphs that show:
- Blue line: Your actual water level readings
- Red dotted line: The danger threshold you set
- Easy to understand trends over time

Perfect for sharing with local authorities or community groups!

**Sample Graph Output:**
When you run the graph command, you'll get a visual chart saved as `graph.png` in your project folder. The graph shows water levels over time with clear markers for each reading.

---

## 📊 Sample Output

Here's what you'll see when you run the list command:

```
Water Level Readings (Total: 2)
================================================
1. Prayagra : 1.8m on 2025-07-01 12:48:52
2. Mumbai : 2.3m on 2025-07-01 13:15:49
================================================
Last updated: 2025-07-12 13:15:49
```

The tool keeps track of everything - city names, water levels, and timestamps. Super easy to understand at a glance!

---

## 🛠️ Setting It Up

**For Replit Users:**
1. Just upload all the files
2. Run: `pip install matplotlib`
3. Start using the commands above!

**For Local Computer:**
1. Make sure you have Python installed
2. Download all files to a folder
3. Run: `pip install matplotlib`
4. You're good to go!

---

## 📂 What's Inside This Project

```
Water-level-monitor/
├── main.py              # The main program (all the magic happens here)
├── data.json            # Where your readings get saved
├── threshold.txt        # Your safety limit
├── graph.png            # Generated graph image (created when you run graph command)
├── requirements.txt     # List of tools needed
├── README.md           # This file you're reading
```

---

## 🌟 Real Stories This Could Help With

**Scenario 1:** *"Our village gets flooded every year. With this tool, we can track patterns and warn people in advance."*

**Scenario 2:** *"I'm doing an environmental project for college. This helps me collect and visualize real water data."*

**Scenario 3:** *"Our apartment complex has drainage issues. Now we can track and show data to the municipality."*

---

## ❤️ A Little About Me

Hi! I'm Shivam, a student who loves solving real problems with code. I built this because I believe technology should help communities, not just big companies. 

This project taught me a lot about:
- Building tools that actually help people
- Making technology accessible to everyone
- Turning ideas into working solutions

Thanks to ChatGPT's guidance, this tool became a real-world utility anyone can use and understand.

You can check out my other projects at: [GitHub.com/shivamdubey0001](https://github.com/shivamdubey0001)

---

## 🚀 Want to Make It Better?

Got ideas? Found a bug? Want to add new features? I'd love to hear from you! Some ideas I'm thinking about:
- SMS alerts when threshold is crossed
- Weather integration
- Mobile app version
- Multi-language support

Feel free to suggest anything!

---

## 📞 Need Help?

If you're stuck anywhere or have questions, just reach out! I'm always happy to help fellow developers and community members.

---

## 🎉 Final Words

This tool is completely free and open for everyone. Use it, modify it, share it - whatever helps your community stay safe!

Remember: Small tools can make big differences. Stay safe, stay informed! 🌊

---

*Made with ❤️ for communities everywhere*