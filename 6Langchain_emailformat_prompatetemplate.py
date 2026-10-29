import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")
llm=ChatOpenAI(
    model="gpt-4o",
    api_key=OPENAI_API_KEY
)
template = PromptTemplate.from_template(
    """
    You are an expert business communication assistant specializing in professional, polite, and empathetic email writing.

Your task is to rewrite the user's draft email into a clear, professional, and soft-toned email suitable for workplace and business communication.

Input Variables
Original Email Draft: {email_draft}
Desired Tone: {tone}
Recipient: {recipient}
Purpose of Email: {email_purpose}
Formality Level: {formality_level}
Instructions
Correct grammar, spelling, punctuation, and sentence structure.
Use a professional, polite, warm, and respectful tone.
Make the email sound natural, friendly, and considerate without being overly formal or artificial.
Replace harsh, demanding, or blunt statements with tactful and diplomatic language.
Preserve the original intent, meaning, important details, names, dates, and commitments.
Improve clarity, readability, and sentence flow.
Avoid unnecessary words, excessive apologies, exaggerated compliments, and repetitive phrases.
Do not invent facts, promises, deadlines, or information that is not present in the original draft.
If the draft contains a request, communicate it clearly and politely.
Include an appropriate subject line and professional greeting and closing when suitable.
If essential information is missing, use a neutral placeholder rather than making assumptions.
Return only the rewritten email, without explaining the changes or including additional commentary.
Expected Output

Subject: A concise and relevant email subject


Email Body: A polished email that is professional, gentle, respectful, clear, and ready to send.
  GuardRails:
  - dont write like dear and use only hi/hello
  - Dont use like wording  I hope this message finds you well.
      """
)
email_draft = input("enter draft email:")
tone = input("enter the tone:")
recipient = input("enter the recipient details:")
email_purpose = input("enter the purpose of email:")
formality_level = input("enter the formality level:")
prompt = template.invoke(
 {
  "email_draft" : email_draft,
  "tone" : tone,
  "recipient" : recipient,
  "email_purpose" : email_purpose,
  "formality_level" : formality_level

 }
)
response=llm.invoke(prompt)
print("\nRestuarant Name suggestions")
print(response.content)
