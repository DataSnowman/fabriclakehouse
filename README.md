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

### Create a Workspace

Click on Workspaces on the left nav bar and click on +New workspace

![newworkspace](https://raw.githubusercontent.com/datasnowman/fabriclakehouse/main/images/newworkspace.png)

Give the workspace a name like fabriclakehouse (or if you have multiple users taking the workshop prehaps add you intials fabriclakehouse-des).  Make sure to chose the Trial License mode under the Advanced area.  Click Apply.

![createws](https://raw.githubusercontent.com/datasnowman/fabriclakehouse/main/images/createws.png)

### Create a Lakehouse

You now should be in your new workspace.  Click on New and choose Lakehouse (Preview).  

![createlh](https://raw.githubusercontent.com/datasnowman/fabriclakehouse/main/images/createlh.png)

This will pop up a New Lakehouse dialog.  Enter a name like medicarepartd and click Create

![lhname](https://raw.githubusercontent.com/datasnowman/fabriclakehouse/main/images/lhname.png)

This will create an open up your new Lakehouse.

```Note that the Lakehouse and the concept aroung OneLake and Delta/Parquet files is the foundation of Data Engineering, Data Science, Data Wareouse, and Real Time Analytics use cases using Fabric```

![explorelh](https://raw.githubusercontent.com/datasnowman/fabriclakehouse/main/images/explorelh.png)

You are now ready to start doing some data engineering.  You are going to first want to create some new subfolders under Files

### Upload some files into the Lakehouse

![newsub](https://raw.githubusercontent.com/datasnowman/fabriclakehouse/main/images/newsub.png)

Enter a name for your new subfolder and click Create

![medicaresf](https://raw.githubusercontent.com/datasnowman/fabriclakehouse/main/images/medicaresf.png)

Add additional subfolders so it looks like this

![subs](https://raw.githubusercontent.com/datasnowman/fabriclakehouse/main/images/subs.png)

You can also use the OneLake Windows Explorer to create subfolders and copy files

![olwe](https://raw.githubusercontent.com/datasnowman/fabriclakehouse/main/images/olwe.png)

Download the Medicare PartD files [here](https://data.cms.gov/provider-summary-by-type-of-service/medicare-part-d-prescribers/medicare-part-d-prescribers-by-provider-and-drug/data/2013) for as many years as you like.  At the time of writing this there were 9 years from 2013 to 2021 available.  You can toggle to the year you want to Export and the top and click export to download the year csv as a zip file.

![exportmpd](https://raw.githubusercontent.com/datasnowman/fabriclakehouse/main/images/exportmpd.png)

Upload all the zip files into the zip subfolder using the OneLake WIndows Explorer or the Fabric lakehouse browser

![upload](https://raw.githubusercontent.com/datasnowman/fabriclakehouse/main/images/upload.png)

All the files should look like this

![zip](https://raw.githubusercontent.com/datasnowman/fabriclakehouse/main/images/zip.png)

### Create a Data Factory Pipeline to unzip and copy the files to the raw folder

Go back into the Workspace and create a new Data pipeline.  Click on Data Pipeline 

![newpl](https://raw.githubusercontent.com/datasnowman/fabriclakehouse/main/images/newpl.png)

Name the pipeline something like `Unzip and Load csv` and click Create

![createpl](https://raw.githubusercontent.com/datasnowman/fabriclakehouse/main/images/createpl.png)

This will open up the Data Factory pipeline.  Click on Add pipeline activity and select Copy data

![copydata](https://raw.githubusercontent.com/datasnowman/fabriclakehouse/main/images/copydata.png)

Give the Copy activity a name like `Unzip and Copy to raw`

![UnzipCopyRaw](https://raw.githubusercontent.com/datasnowman/fabriclakehouse/main/images/UnzipCopyRaw.png)

On the Source tab choose the Workspace, Lakehouse, Files, and File Path and browse to the zip folder and click Ok

![sourcebrowse](https://raw.githubusercontent.com/datasnowman/fabriclakehouse/main/images/sourcebrowse.png)

Your source choice should look like this:

File path: `medicare/zip`

Recursively: checked

File Format: Binary

Click on Settings and select Compression Type: `ZipDeflate (.zip)`

Preserve zip file name as folder: unchecked

![sourceunzip](https://raw.githubusercontent.com/datasnowman/fabriclakehouse/main/images/sourceunzip.png)

On the Destination tab choose the Workspace, Lakehouse, Files, and File Path and browse to the raw folder and click Ok

File path: `medicare/raw`

File Format: Binary

![destinationraw](https://raw.githubusercontent.com/datasnowman/fabriclakehouse/main/images/destinationraw.png)

Save and Run the pipeline

![inprogress](https://raw.githubusercontent.com/datasnowman/fabriclakehouse/main/images/inprogress.png)

The pipeline will take the zipfiles in `medicare/zip`

![zipfiles](https://raw.githubusercontent.com/datasnowman/fabriclakehouse/main/images/zipfiles.png)

And when succeeded

![succeeded](https://raw.githubusercontent.com/datasnowman/fabriclakehouse/main/images/succeeded.png)

And uzip them to `medicare/raw`

![unzippedfiles.png](https://raw.githubusercontent.com/datasnowman/fabriclakehouse/main/images/zipfiles.png)

### Load all the files into a Delta Table using a Data Engineering Notebook

To get a copy of the `LoadMedicarePartDfiles.ipynb` notebook either click [here](https://github.com/DataSnowman/fabriclakehouse/tree/main/medicarepartd/code/notebook) and download the notebook.  Or you can clone the GitHub Repo to your desktop

```
git clone https://github.com/DataSnowman/fabriclakehouse.git
```
Import the notebook into the workspace by navigating to the Data Engineering home and clicking on Import notebook 

![importnb](https://raw.githubusercontent.com/datasnowman/fabriclakehouse/main/images/importnb.png)

Click Upload and select the notebook and click Open

![uploadnb](https://raw.githubusercontent.com/datasnowman/fabriclakehouse/main/images/uploadnb.png)

Click on Go to workspace

![gotows](https://raw.githubusercontent.com/datasnowman/fabriclakehouse/main/images/gotows.png)

Click on the `LoadMedicarePartDfiles` notebook

![loadmpdfiles](https://raw.githubusercontent.com/datasnowman/fabriclakehouse/main/images/loadmpdfiles.png)

If it does not open up in the lakehouse click Add below Add lakehouse

![addlh](https://raw.githubusercontent.com/datasnowman/fabriclakehouse/main/images/addlh.png)

Choose Existing lakehouse Add button

![existinglh](https://raw.githubusercontent.com/datasnowman/fabriclakehouse/main/images/existinglh.png)

Choose the data you want to connect
and click Add

![choosedata](https://raw.githubusercontent.com/datasnowman/fabriclakehouse/main/images/choosedata.png)

Now your notebook should look like this:

![nbtorun](https://raw.githubusercontent.com/datasnowman/fabriclakehouse/main/images/nbtorun.png)

The first two cells of the notebook include schemas for the csvs and for the Delta/Parquet table

![2cells](https://raw.githubusercontent.com/datasnowman/fabriclakehouse/main/images/2cells.png)

The third cell has the logic for loading the 9 csv files

![3rdcell](https://raw.githubusercontent.com/datasnowman/fabriclakehouse/main/images/3rdcell.png)

You can chose to run one cell at a time or click on Run all.  It will take about 20-25 minutes for the tables to load

When it is running you may get some messages like this since the files have a number of null columns.  This is fine.

![nbrunning](https://raw.githubusercontent.com/datasnowman/fabriclakehouse/main/images/nbrunning.png)

The notebook creates the medicarepartd Delta table in the Lakehouse

![medicarepartdtable](https://raw.githubusercontent.com/datasnowman/fabriclakehouse/main/images/medicarepartdtable.png)


### Open and query the Delta Table using the Lakehouse SQL endpoint

In the top right corner of the Lakehouse interface you can switch to the SQL Endpoint

![switchtosqlep](https://raw.githubusercontent.com/datasnowman/fabriclakehouse/main/images/switchtosqlep.png)

The Delta table automatically creates a SQL Table that can be queried with SQL

![sqlep](https://raw.githubusercontent.com/datasnowman/fabriclakehouse/main/images/sqlep.png)

Click on New query

![newquery](https://raw.githubusercontent.com/datasnowman/fabriclakehouse/main/images/newquery.png)

Copy the existing query to count the rows loaded by fourdigityear which represents the number of rows in each yearly csv file

```
SELECT fourdigityear, count(Prscrbr_NPI) as numrows FROM medicarepartd GROUP BY fourdigityear
``````

Click Run

![rowsbyyear](https://raw.githubusercontent.com/datasnowman/fabriclakehouse/main/images/rowsbyyear.png)

If you highlight the SQL statement
you can click Save as view to create a view

![saveasaview](https://raw.githubusercontent.com/datasnowman/fabriclakehouse/main/images/saveasaview.png)

Click OK 

![viewname](https://raw.githubusercontent.com/datasnowman/fabriclakehouse/main/images/viewname.png)

Find the view and look at the data prreview

![viewdatapreview](https://raw.githubusercontent.com/datasnowman/fabriclakehouse/main/images/viewdatapreview.png)

### Look at the SQL Endpoint Model

From what you have done in the Lakehouse so far you should have 2 tables in the Model.  One is the Delta table `medicarepartd` you created with the notebook and the second is the view you created in the SQL Endpoint `countofrowsbyyear`

![model](https://raw.githubusercontent.com/datasnowman/fabriclakehouse/main/images/model.png)

Now like in Power BI Desktop this is where you would create the model you use in Power BI.  For now we will keep it separate and just hide the `countofrowsbyyear` and just use the one big table.

To hide the view click on the eye looking icon in the top right corner of the view.  This will put a \ across the icon and hide the view.

![hideview](https://raw.githubusercontent.com/datasnowman/fabriclakehouse/main/images/hideview.png)

### Autocreate a Report

This will become the default dataset in your Workspace for this Lakehouse.  Navigate back to the workspace to find the default dataset

![defaultds](https://raw.githubusercontent.com/datasnowman/fabriclakehouse/main/images/defaultds.png)

Click on the 3 dots at the end of the name of the medicarepartd default data set.  Just to the left of the Type dataset (default).

Click on Autocreate Report

![autocreatereport](https://raw.githubusercontent.com/datasnowman/fabriclakehouse/main/images/autocreatereport.png)

Give it a couple minutes and `bam` you have created your first report

![autoreport](https://raw.githubusercontent.com/datasnowman/fabriclakehouse/main/images/autoreport.png)

Click on save then name the report `autoreport` and click save

![savereport](https://raw.githubusercontent.com/datasnowman/fabriclakehouse/main/images/savereport.png)

If you look back in your workspace you will see your first report

![savefirstreport](https://raw.githubusercontent.com/datasnowman/fabriclakehouse/main/images/savefirstreport.png)


### Create more of a star schema using a notebook

The next thing you are going to do is cut up the one big table and transform the data into a fact table and some dimension tables.  We are going to do this in a Notebook and then create a new dataset with the new tables.

To get a copy of the `Load cms_provider_fact_star.ipynb` notebook either click [here](https://github.com/DataSnowman/fabriclakehouse/tree/main/medicarepartd/code/notebook) and download the notebook.  Or you can clone the GitHub Repo to your desktop

```
git clone https://github.com/DataSnowman/fabriclakehouse.git
```
Import the notebook into the workspace by navigating to the Data Engineering home and clicking on Import notebook 

![importnb](https://raw.githubusercontent.com/datasnowman/fabriclakehouse/main/images/importnb.png)

Click Upload and select the notebook and click Open

![uploadnb2](https://raw.githubusercontent.com/datasnowman/fabriclakehouse/main/images/uploadnb2.png)

Click on Go to workspace

![gotows](https://raw.githubusercontent.com/datasnowman/fabriclakehouse/main/images/gotows.png)

Click on the `Load cms_provider_fact_star` notebook

![loadstarnb](https://raw.githubusercontent.com/datasnowman/fabriclakehouse/main/images/loadstarnb.png)

If it does not open up in the lakehouse click Add below Add lakehouse

![addlh](https://raw.githubusercontent.com/datasnowman/fabriclakehouse/main/images/addlh.png)

Choose Existing lakehouse Add button

![existinglh](https://raw.githubusercontent.com/datasnowman/fabriclakehouse/main/images/existinglh.png)

Choose the data you want to connect
and click Add

![choosedata](https://raw.githubusercontent.com/datasnowman/fabriclakehouse/main/images/choosedata.png)

Now your notebook should look like this:

![nb2torun](https://raw.githubusercontent.com/datasnowman/fabriclakehouse/main/images/nb2torun.png)

The note book contains a series of cells that first create a Spark TEMPORARY VIEW like `cms_provider_dim_drug_lhvw`

And then create a new Delta Table using that temporary view

![tempviewdeltacells](https://raw.githubusercontent.com/datasnowman/fabriclakehouse/main/images/tempviewdeltacells.png)

You can chose to run one cell at a time or click on Run all.  It will take about 20 minutes for the tables to load

The notebook creates the new fact and dimension Delta tables in the Lakehouse.

![dimandfacttables](https://raw.githubusercontent.com/datasnowman/fabriclakehouse/main/images/dimandfacttables.png)


The SQL takes advantage of the Over clause and creates tables the way you typically would in a MPP Data Warehouse.  I got this code from one of my peers in Health and life sciences.  I don't fully understand the logic of creating the dimensions and I will try to (in the future) update this code with and option of creating slowly changing dimensions using MD5 hash for primary surogate keys and effective dates and then load the fact table using those surogate keys.  Lots of thought and work to be done for this however.

### Create a new Power BI dataset

In the Lake house click on `New Power BI dataset`

Select the dimensions and fact table and click Confirm

![newdsdialog](https://raw.githubusercontent.com/datasnowman/fabriclakehouse/main/images/newdsdialog.png)

Here are the tables

![startables](https://raw.githubusercontent.com/datasnowman/fabriclakehouse/main/images/startables.png)

Create the join relationships

Start with the key in the fact and drag it to the key in the dimension. Click the Assume referential integrity box and click Confirm

![relationships](https://raw.githubusercontent.com/datasnowman/fabriclakehouse/main/images/relationships.png)

year to year
drug_key to drug_key
geo_key to geo_key
provider_key to provider_key

![star](https://raw.githubusercontent.com/datasnowman/fabriclakehouse/main/images/star.png)

Give the dataset a name like `medicarepartdstar`

![medicarepartdstar](https://raw.githubusercontent.com/datasnowman/fabriclakehouse/main/images/medicarepartdstar.png)

Back in the workspace filter on Dataset and find you new dataset

![medicarepartdstards](https://raw.githubusercontent.com/datasnowman/fabriclakehouse/main/images/medicarepartdstards.png)

Click on the new dataset and see all the options you have.  Go ahead and try to:

    - Create a report
    - Create paginated report


![dsoptions](https://raw.githubusercontent.com/datasnowman/fabriclakehouse/main/images/dsoptions.png)

### Put the Data factory pipeline all together

`Note: This was a bit finicy when I ran this on my trial capacity.  I needed to use a Fabric Capacity I created in the Azure Portal to get  the pipeline to run the notebook activities successfully`

