## Creating Environment variables
   Create a .env file in root and variables
   POSTGRES_USER=SOMETHING
   POSTGRES_PASSWORD=SOMEPASSWORD
 
## Loading environment variables

   from dotenv import load_dotenv
   load_dotenv()
   
## Usage
    os.environ['POSTGRES_USER']

