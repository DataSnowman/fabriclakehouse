# Microsoft Fabric Fundamentals Workshop (fabriclakehouse)
Use this repo for learning and skilling related to Microsoft Fabric Fundamentals

Welcome to the workhop.  The purpose of the workshop is to bring you up to speed on some of the Lakehouse, Data Engineering, Data Science, and Data Analysis capabilities of Microsoft Fabric.  You will be using resources in a Microsoft Fabric tenant and in an Azure Subscription for this workshop.  As a result you could use this for training as an individual or group who have access to a Microsoft Fabric Workspace. Potentially if using other Azure services like Azure Data Lake Storage, Azure Databricks, Azure SQL Database, and Azure SQL Managed Instance you would also need an Azure Subscription.

The Workshop is broken into multiple parts by Fabric Analytic Workloads:

Part 1: Lakehouse and Data Engineering

    - Lakehouse
    
    - Data Factory (Data Integration)
    
    - Data Engineering

    - Power BI (Data Analysis)

Part 2: Lakehouse and Data Science (To be added)  
    
    - Data Science

Part 3: Data Warehouse (To be added)    

    - Data Warehouse

    - Power BI (Data Analysis)

Part 4: Real Time Analytics (To be added)

    - Real Time Analytics

    - Power BI (Data Analysis)

    
## Data Sources 

The workshop also incorporates a number of data sources like:

Public

[Centers for Medicare & Medicai Services data.cms.gov](https://data.cms.gov/)

* [Medicare Part D Prescribers - by Provider and Drug](https://data.cms.gov/provider-summary-by-type-of-service/medicare-part-d-prescribers/medicare-part-d-prescribers-by-provider-and-drug/data/2013)

Personal

[Some data off of my PC when playing Minecraft](https://www.minecraft.net/en-us/store/minecraft-deluxe-collection-pc)

## Sections (Parts)

[Part 1: Lakehouse and Data Engineering](https://github.com/DataSnowman/fabriclakehouse/tree/main#part-1-lakehouse-and-data-engineering)


[Part 2: Lakehouse and Data Science (To be added)](https://github.com/DataSnowman/fabriclakehouse/tree/main#sections-parts)

[Part 3: Data Warehouse (To be added)](https://github.com/DataSnowman/fabriclakehouse/tree/main#sections-parts)

[Part 4: Real Time Analytics (To be added)](https://github.com/DataSnowman/fabriclakehouse/tree/main#sections-parts)

```Note: to use Microsoft Fabric in your Power BI Tenant your Power BI admin is going to need to enable the Microsoft Fabric Trial```

## Part 1: Lakehouse and Data Engineering

Log into Microsoft Fabric at https://fabric.microsoft.com with your Azure Active Directory userid (work email) and password.  Same one you use to access M365.

![fabrichome](https://raw.githubusercontent.com/datasnowman/fabriclakehouse/main/images/fabrichome.png)

Since we want to create a lakehouse and do data engineering tasks click on the Microsoft Fabric icon in the bottom left corner and select Data Engineering

![fabricicon](https://raw.githubusercontent.com/datasnowman/fabriclakehouse/main/images/fabricicon.png.png)

`Note: If you have not been assigned a Fabric Workspace you may need to create one.  If you are taking a training with and an instructor please check with your instructor.`

Click on Workspaces on the left nav bar and click on +New workspace

![newworkspace](https://raw.githubusercontent.com/datasnowman/fabriclakehouse/main/images/newworkspace.png)

Give the workspace a name like fabriclakehouse (or if you have multiple users taking the workshop prehaps add you intials fabriclakehouse-des).  Make sure to chose the Trial License mode under the Advanced area.  Click Apply.

![createws](https://raw.githubusercontent.com/datasnowman/fabriclakehouse/main/images/createws.png)

You now should be in your new workspace.  Click on New and choose Lakehouse (Preview).  

![createlh](https://raw.githubusercontent.com/datasnowman/fabriclakehouse/main/images/createlh.png)

This will pop up a New Lakehouse dialog.  Enter a name like medicarepartd and click Create

![lhname](https://raw.githubusercontent.com/datasnowman/fabriclakehouse/main/images/lhname.png)

This will create an open up your new Lakehouse.

```Note that the Lakehouse and the concept aroung OneLake and Delta/Parquet files is the foundation of Data Engineering, Data Science, Data Wareouse, and Real Time Analytics use cases using Fabric```

![explorelh](https://raw.githubusercontent.com/datasnowman/fabriclakehouse/main/images/explorelh.png)

You are now ready to start doing some data engineering.  You are going to first want to create some new subfolders under Files

![newsub](https://raw.githubusercontent.com/datasnowman/fabriclakehouse/main/images/newsub.png)

Enter a name for your new subfolder and click Create

![medicaresf](https://raw.githubusercontent.com/datasnowman/fabriclakehouse/main/images/medicaresf.png)

Add additional subfolders so it looks like this

![subs](https://raw.githubusercontent.com/datasnowman/fabriclakehouse/main/images/subs.png)

You can also use the OneLake Windows Explorer to create subfolders and copy files

![olwe](https://raw.githubusercontent.com/datasnowman/fabriclakehouse/main/images/olwe.png)

Download the

