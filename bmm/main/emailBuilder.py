from __future__ import print_function
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
onfiguration = sib_api_v3_sdk.Configuration()
configuration.api_key['api-key'] = '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'
api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))
subject = "Can you help us?"
sender = {"name":"Sendinblue","email":"contact@sendinblue.com"}
replyTo = {"name":"Sendinblue","email":"bmmsuppo@gmail.com"}
html_content = "<html><body><h1>This is my first transactional email </h1></body></html>"
to = [{"email":"example@example.com","name":"Jane Doe"}]
params = {"parameter":"My param value","subject":"New Subject"}
send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(to=to, bcc=bcc, cc=cc, reply_to=reply_to, headers=headers, html_content=html_content, sender=sender, subject=subject)

try:
    api_response = api_instance.send_transac_email(send_smtp_email)
    print(api_response)
except ApiException as e:
    print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)