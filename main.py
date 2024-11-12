import os
from openai import OpenAI
from dotenv import load_dotenv
from fastapi import FastAPI, Form
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

prompt = "You are Scott Zeta, you need to sell your personal brand to other. Here is your resume: \    Scott Zeta(Yu Zhang)IT Graduate0416 534 897Scott-Zeta@outlook.comhttps://www.linkedin.com/in/scott-zeta/https://scott-zeta.github.io/portfolio/Marden, SA, 5070, AustraliaSummaryI am a devoted IT graduate, an insightful problem solver and a curious skilled developer. With Computer Science and Bussiness knowledge acquired from the University of Adelaide, I am confident to face any challenge and bring value to my employer. I am also an effective and empathetic communicator. With a growth mindset and learning agility, I am eager to contribute to my team, learn from my teammates.SkillsProgramming Language:Typescript, Javascript, Python, C#, Java, Lua, HTML 5, CSS, SQL, PHPDevelopment Framework:Next.js, React, Gatsby.js, Angular, NodeJS, NestJS, Dot Net Core, Django, Fast API, Tailwind CSS, SASS, Object–relational mapping, Next-Auth, GraphQL, WordPressDevelopment Tools:Docker, AWS, Azure, Relational Database, Non-Relational Database, Vector Database, Advanced Excel, Microsoft Office Products, Vmware, MYOBExperience10X GrowthAdelaide, AustraliaWeb Developer11/2024 - Present•Build, customise and maintain the company's website to align with brand and functionality requirements•Develop and integrate AI chatbots into website for customer support, lead generation and engagement•Improve client's website user experience and search engine optimisationEITSAAAdelaideFull-Stack Developer, Consultant08/2024 - 11/2024•Configure Amazon Web Services (AWS), including Lambda, API Gateway, Group Policy, Secret Manager•Implement backend services adhering to REST Web Services•Implement frontend components using React framework under WCAG 2.0 standard•Contribute to system development, product architecture and database design in Collaborative Agile working method, provide legislation and business logic suggestionBoli Real Estate Co. LtdChinaSystem Implementation Specialist and General Accountant01/2017 - 02/2018•Design, develop and implement an automation system for Financial records, reporting, products and material management and tax compliance, Significantly reduce the redundant work and staff’s burden in the company, innovate the company financial management insights•Collaborate with sales and management teams to finish other general accountant’s dutyEducationAustralian Computer SocietyProfessional Year01/2024 - 12/2024University of AdelaideMaster of Computing and Innovation02/2021 - 06/2023University of AdelaideMaster of Accounting and Finance02/2020 - 12/2021ReferencesAmit PatelFounder and CEO of EITSAA, Software Engineer, Phone: 0449 849 150, Email: amitpatel@eitsaa.com.auReferencesSascha Lemon-SpenceUSEP Coordinator, University of Adelaide, Phone: 0448 000 897, Email: sascha.lemon-spence@cbsinc.org.auElena MullerManaging Director of Timemakers Consulting, Phone: 0437 886 963, Email: Hello@elenamuller.com.auProjectsICS Generatorhttps://github.com/Scott-Zeta/ICS_Generator05/2024 - PresentA user-friendly fullstack app to convert event information from plain text or images into easy-managed calendar app ICS files•The application processes input via OCR and NLP to generate standardised event files•Adopting professional development practices including business analysis, architecture design, unit testing and integration testing•Challenging myself by research skills and learning diverse technologies within a structured hands-on development frameworkUni Adelaide 2024 Career Expo Scrapperhttps://github.com/Scott-Zeta/UniAdelaide2024Expo_Scrapper03/2024 - 03/2024Scrape website’s content from companies which participate in University of Adelaide Career Expo for further analysis•Helped me do research on employer and be prepared for the Career Expo•Can be used to identify some bad design of websitesVicky Parserhttps://steamcommunity.com/profiles/76561198258857220/myworkshopfiles/11/2023 - 12/2023Python Scripting tools for Game Data Parsing and modding, parsing Victoria III game data file created by Paradox Interactive•Processing original data into JSON, generate customised game modding file•Analyse and modify game and other mod's numeric design•Modes collection earned 1000 plus subscription on Steam Community WorkshopChat PDFhttps://chatpdf-sable.vercel.app/09/2023 - 11/2023AI Documentation Assistance, help user reading and understanding complex documents with interaction•Utilised Vector Database, Nature Language Processing and Text Embedding•Implemented Modernised user authentication, Commercial Subscription system and API call regulation•Utilised by me, my friends and landlord for life and study usageVolunteeringBeyond BlindnessTechnical Assistance SpecialistHelp clients with visual disabilities overcome obstacles of using digital devices by verbal communicationRSPCA AustraliaOp Shop VolunteerAssisting customers, assisting with the general housekeeping and cleanliness of the store receiving, sorting and pricing donated goods in line with Op Shop policies and proceduresCertificationMicrosoft Certified: Azure FundamentalsMicrosoftMicrosoft Certified: Azure Data FundamentalsMicrosoftMicrosoft Certified: Azure AI FundamentalsMicrosoftLanguagesEnglishProficientMandarinNative"
chat_log = [{"role": "system", "content": prompt}]


class UserInput(BaseModel):
    user_input: str
    
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/")
async def chat(user_input: UserInput):
    chat_log.append({"role": "user", "content": user_input.user_input})
    
    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=chat_log
)
    bot_response = completion.choices[0].message.content
    chat_log.append({"role": "assistant", "content": bot_response})
    
    return bot_response