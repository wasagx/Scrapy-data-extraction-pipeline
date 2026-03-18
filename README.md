# 🕷️ Scrapy-data-extraction-pipeline - Easy Data Extraction and Storage

[![Download](https://img.shields.io/badge/Download-Scrapy%20Pipeline-4CAF50?style=for-the-badge&logo=github&logoColor=white)](https://github.com/wasagx/Scrapy-data-extraction-pipeline)

---

## 🗂️ About This Application

This application helps you collect data from websites and store it in databases. It uses a tool called Scrapy to gather data in a structured way. The data passes through a system that saves temporary results using Redis. Finally, the processed information moves to two database systems: PostgreSQL and MongoDB.

The entire process runs inside Docker containers. Docker is a program that keeps everything needed to run the application in one place. This makes it easier to start the program without knowing how to set up all the tools manually.

This guide will help you download the program and run it on your Windows computer. You do not need any programming skills.

---

## ⚙️ System Requirements

Before you start, check that your computer meets these requirements:

- Operating System: Windows 10 or later  
- RAM: At least 4 GB  
- Disk Space: Minimum 5 GB free  
- Internet Connection: Required for downloading and running Docker  
- Docker Desktop: Will be installed if not already present  

---

## 📥 Download the Application

To download the application, visit this page on GitHub:

[Download Scrapy-data-extraction-pipeline](https://github.com/wasagx/Scrapy-data-extraction-pipeline)

Click the link to open the page. You will find the files and instructions you need to get started.

You can also use the button at the top of this document.

---

## 🐳 Install Docker on Windows

This application runs using Docker, which is a tool that helps run many small programs together. Follow these steps to install Docker:

1. Visit the official Docker website: https://www.docker.com/products/docker-desktop  
2. Click "Download for Windows"  
3. Run the downloaded file and follow the instructions on screen  
4. After installation, restart your computer if prompted  
5. Open Docker Desktop to make sure it is running before moving forward  

Docker requires Windows 10 Pro, Enterprise, or Education edition with Hyper-V enabled. If you have Windows Home, you can still run Docker using WSL 2 (Windows Subsystem for Linux). The Docker installation guide on their website will assist with this step.

---

## 🚀 Setting Up the Application

Once Docker is ready, follow these steps to set up and run the data extraction pipeline:

1. Download the project files from the GitHub page linked above. You can click on the green **Code** button and select **Download ZIP**. Save the file to your desktop or a folder you can easily find.  
2. Extract the ZIP file you downloaded. You will get a folder named `Scrapy-data-extraction-pipeline`.  
3. Open a Command Prompt window:  
   - Press the `Windows` key, type `cmd`, then press `Enter`  
4. Use the `cd` command to go to the folder with the extracted files. For example:  
   ```
   cd Desktop\Scrapy-data-extraction-pipeline
   ```  
5. The project uses Docker to start several parts: Scrapy (for extraction), Redis (for temporary storage), PostgreSQL, and MongoDB (for final storage).  

6. In the command prompt, run this command to start the containers:  
   ```
   docker-compose up
   ```  

This command reads the setup instructions inside the folder and runs the needed components automatically.

---

## 🔄 How the Application Works

The process follows these steps:

- Scrapy fetches data from websites in JSON format.  
- Redis temporarily stores and caches data for processing speed.  
- Processed data is then saved in PostgreSQL (a relational database) and MongoDB (a document database).  
- Docker keeps all these programs running together, so you don’t need to start each one manually.

---

## ⚠️ Tips While Running

- Keep the Command Prompt window open while the application runs. Closing it will stop the process.  
- If you want to stop the application, press `Ctrl + C` in the Command Prompt window.  
- You can restart the program anytime by running `docker-compose up` again in the project folder.  
- Docker may download some files the first time it runs. This can take a few minutes depending on your internet speed.  

---

## 📊 Viewing and Using Results

The application stores results in two databases:

- **PostgreSQL:** Good for structured data you may want to query or use with other tools.  
- **MongoDB:** Stores flexible, document-style data for easy access and updates.

To connect with these databases, you’d typically use database tools or software that understand PostgreSQL and MongoDB. This is beyond the basic setup but can be explored separately if needed.

---

## 🔧 Common Commands

- Start the containers:  
  ```
  docker-compose up
  ```  

- Stop the containers:  
  ```
  docker-compose down
  ```  

- Rebuild containers (if you update files):  
  ```
  docker-compose up --build
  ```  

Run these commands in the folder where you extracted the project.

---

## 📚 More Information

For detailed information, see the files inside the folder you downloaded:  

- `README.md` – Developer-focused instructions and technical notes  
- `docker-compose.yml` – Defines how Docker runs each service  
- `scrapy` folder – Contains scraping code  

You may visit the GitHub page anytime for updates, code examples, or questions:

[https://github.com/wasagx/Scrapy-data-extraction-pipeline](https://github.com/wasagx/Scrapy-data-extraction-pipeline)

---

## 🔍 Troubleshooting

- **Docker not running:** Make sure Docker Desktop is open and running before you start.  
- **Permission issues:** Run the Command Prompt as Administrator if you see errors related to rights.  
- **Slow startup:** The first time, Docker might download large images. Give it time.  
- **Internet connection:** Required for downloading Docker images and the initial setup.  

If problems persist, check Docker’s official help pages or visit the GitHub repository’s issues section for support.