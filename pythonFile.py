import ast
import json
import os
import random
import re
import string
import sys
import time
import traceback
from datetime import datetime
from datetime import timedelta

import curlify
import jwt
import redis
import requests
import urllib3
from redis import Sentinel
from robot.api import logger
from robot.libraries.BuiltIn import BuiltIn
from robot.libraries.DateTime import Date

urllib3.disable_warnings()
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Common')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Email')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Planner', 'DB')))
from Planner_Data import *
from JsonLib import *
from DB import *
from Email import *
arg = sys.argv[1]
# arg = 'dev'


def generate_token_automation(env=arg):
    email = os.environ.get('email')
    password = os.environ.get('password')
    endpoint_url = "https://gateway-service-" + str(env) + ".deepintent.com/graphql"
    headers = {'Content-Type': 'application/json', 'accept': '*/*'}

    data = '{"query":"mutation{generateToken(tokenInput:{applicationId:2,grantType: Password,credentials:{emailOrClientId:\\"input_email\\",passwordOrClientSecret:\\"input_pass\\"}}){accessToken refreshToken } }"}'
    data = data.replace('input_email', email)
    data = data.replace('input_pass', password)
    # builtlib = BuiltIn().get_library_instance("BuiltIn")
    response = requests.post(endpoint_url, headers=headers, data=data, verify=True)

    new = json.loads(response.content)
    token = 'Bearer '
    token = token + new['data']['generateToken']['accessToken']
    print(token + ',' + endpoint_url)


class CommonAPI:
    def __init__(self):
        try:
            self.builtlib = BuiltIn().get_library_instance("BuiltIn")
            self.db = DB()
            self.email = Email()
            self.planner_data = Planner_Data()
        except:
            self.logger("info",sys.exc_info())

    def generate_token(self, **kwargs):
        try:
            self.logger("info","inside generate_token")
            email = os.environ.get('email')
            password = os.environ.get('password')
            proxies = os.environ.get('proxies')
            if kwargs.get('email', None) is not None:
                email_ = kwargs.get('email')
                email = os.environ.get(email_)
            if kwargs.get('password', None) is not None:
                password_ = kwargs.get('password')
                password = os.environ.get(password_)
            self.logger("info",email)
            self.logger("info",password)

            endpoint_url = self.endpoint(**kwargs)

            headers = {'Content-Type': 'application/json', 'accept': '*/*'}

            data = '{"query":"mutation{generateToken(tokenInput:{applicationId:2,grantType: Password,credentials:{emailOrClientId:\\"input_email\\",passwordOrClientSecret:\\"input_pass\\"}}){accessToken refreshToken } }"}'
            data = data.replace('input_email', email)
            data = data.replace('input_pass', password)
            self.logger("info",data)
            response = requests.post(endpoint_url, headers=headers, data=data, verify=True, proxies=proxies)
            self.logger("info",response.content)

            new = json.loads(response.content)

            BuiltInlib = BuiltIn().get_library_instance("BuiltIn")
            token = 'Bearer '
            token = token + new['data']['generateToken']['accessToken']
            BuiltInlib.set_suite_variable('${token}', token)
            return token

        except:
            self.logger("info","token generation failed")
            tb = traceback.format_exc()
            self.raise_exception(tb)
        finally:
            self.logger("info","token generation completed")

    def get_api_response(self, dict):
        try:
            self.logger("info","get_api_response Function started")
            kwargs = self.set_headers(dict)
            response = self.set_response(kwargs)
            self.logger("info","get_api_response Function passed")
            return response
        except:
            self.logger("error","get_api_response Function failed")
            tb = traceback.format_exc()
            self.raise_exception(tb)
        finally:
            self.logger("info","get_api_response Function completed")

    def log_api_response_time(self, response=None, payload=None):
        try:
            total_time = response.elapsed.total_seconds()
            if payload is not None:
                response_data = json.loads(payload)
                operation_name = response_data.get('operationName')
                self.logger("info",operation_name)
                self.logger("info","api name : {operation_name} time taken : {total_time}".format(operation_name=operation_name,total_time=total_time))
            else:
                self.logger("info","api name : None time taken : {total_time}".format(total_time=total_time))
        except:
            self.logger("error","log_api_response_time method failed. ->\n response : {response}\npayload :  {payload}\n ".format(payload=str(payload),response=str(response)))


    def set_headers(self, kwargs):
        try:
            self.logger("info","set_headers Function started")

            org_id = kwargs.get('org_id', '10000')
            resourceID = kwargs.get('resourceID', '3')
            applicationId = kwargs.get('applicationID', '2')

            # generate token
            token = self.builtlib.get_variable_value('${token}')
            endpoint_url = self.builtlib.get_variable_value('${endpoint_url}')
            env = BuiltIn().get_variable_value('${ENV}')
            self.logger("info",token)
            self.logger("info",endpoint_url)
            raw_payload = kwargs.get('raw_payload', None)
            data = kwargs.get('payload', None)
            # If token is empty
            if token is None or token == '' or endpoint_url is None:
                token = self.generate_token()
                token = self.builtlib.get_variable_value('${token}')
                endpoint_url = self.builtlib.get_variable_value('${endpoint_url}')
            if env is not None:
                endpoint_url = endpoint_url.replace("dev", env)
                logger.info("endpoint_url="+str(endpoint_url))
            kwargs.update({'token': token})
            kwargs.update({'endpoint_url':endpoint_url})

            common_headers = {'content-type': 'application/json', 'x-resourceId': str(resourceID), 'x-organizationid': org_id,
                       'authorization': token, 'x-applicationid': str(applicationId) ,'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}

            headers = kwargs.get('headers',{})
            headers = {key.lower(): value for key, value in headers.items()}
            common_headers.update(headers)
            kwargs.update({'headers': common_headers})

            self.logger("info","set_headers Function passed")
            return kwargs
        except:
            self.logger("error","set_headers Function failed")
            tb = traceback.format_exc()
            self.raise_exception(tb)
        finally:
            self.logger("info","set_headers Function completed")

    def set_response(self, kwargs):
        try:
            self.logger("info","set_response function started.")
            endpoint_url = kwargs.get('endpoint_url')
            headers = kwargs.get('headers',{})
            data = kwargs.get('payload')

            response = requests.post(endpoint_url, headers=headers, data=data, verify=True,
                                     proxies=self.builtlib.get_variable_value('${proxies}'))
            self.log_api_response_time(response=response,payload=data)
            if response.status_code != 200 or 'error' in str(response.text).lower() or 'exception' in str(response.text).lower() :
                self.logger("error","Got other than success response with status code = {} or error in response".format(response.status_code))
                self.logger("error","curl request : {}".format(curlify.to_curl(response.request)))
                self.logger("error","api str(response) : {}".format(str(response.text)))
                #raise Exception("error response : {}".format(response.content))
            self.logger("info","API response : {api_resp}".format(api_resp=str(response.text)))
            #new = json.loads(response)
            self.logger("info","set_response function passed.")
            return response
        except:
            self.logger("error","set_response function failed")
            tb = traceback.format_exc()
            self.raise_exception(tb)
        finally:
            self.logger("info","set_response function completed")

    def endpoint(self, **kwargs):
        try:
            protocol = os.environ.get('protocol')
            # domain = self.builtlib.get_variable_value('${services_url}')
            domain = os.environ.get('services_url')
            port = kwargs.get('port', 0)

            BuiltInlib = BuiltIn().get_library_instance("BuiltIn")
            print(port)
            if port == 0:
                url = protocol + "://" + domain + "/graphql"
            else:
                url = protocol + "://" + domain + ":" + str(port) + "/graphql"

            BuiltInlib.set_suite_variable('${endpoint_url}', url)
            return url

        except:
            self.logger("error","endpoint generation failed")
            tb = traceback.format_exc()
            self.raise_exception(tb)
        finally:
            self.logger("info","endpoint generation completed")

    def get_resource_id(self, **kwargs):

        try:
            organizationId = kwargs.get('organizationId', False)
            resourceValue = kwargs.get('resourceId', False)

            if organizationId and resourceValue:

                resource_query = 'select resourceId from  common.RESOURCE where organizationId = {organization_id} ' \
                                 'and resourceValue = {resourceValue};'.format(organization_id=organizationId,
                                                                               resourceValue=resourceValue)
                resource_query_data = self.db.execute_query(db_query=resource_query)

                self.logger("info","Resource query : {resource_query} ".format(resource_query=resource_query))
                self.logger("info","Resource id from query is :: {res_id}".format(res_id=resource_query_data))
            else:
                raise Exception("advertiser or publisher for resourceId calculation is missing in parameters")

            return str(resource_query_data[0][0])

        except:
            tb = traceback.format_exc()
            self.raise_exception(tb)

    def get_audit_log_file_name_api(self, **kwargs):
        # try:
        token = self.builtlib.get_variable_value('${token}')
        endpoint_url = self.builtlib.get_variable_value('${endpoint_url}')
        proxies = os.environ.get('proxies')
        # If token is empty
        if token is None or token == '' or endpoint_url is None:
            self.generate_token()
            token = self.builtlib.get_variable_value('${token}')
            endpoint_url = self.builtlib.get_variable_value('${endpoint_url}')
        organization_id = kwargs.get('organization_id')
        advertiser_id = kwargs.get('advertiser_id')
        resource_id = kwargs.get('resource_id')
        application_id = kwargs.get('application_id')
        start_date = kwargs.get('start_date')
        end_date = kwargs.get('end_date')
        entityTypeValue = kwargs.get('entityTypeValue')
        orderId = kwargs.get('orderId')

        start_date = self.add_days_to_date(start_date=start_date)
        end_date = self.add_days_to_date(end_date=end_date)

        users_id = self.get_audit_log_users(**kwargs)
        if organization_id and resource_id:
            resource_query = 'select resourceId from  common.RESOURCE where organizationId = {organization_id} and resourceValue = {resource_value};'.format(
                organization_id=organization_id, resource_value=advertiser_id)
            resource_query_data = self.db.execute_query(db_query=resource_query)
            self.logger("info","Resource query : {resource_query} ".format(resource_query=resource_query))
            self.logger("info","Resource id from query is :: {res_id}".format(res_id=resource_query_data))
        else:
            raise Exception("advertiser or publisher for resourceId calculation is missing in parameters")
        payload = "{\"operationName\":\"downloadAuditLog\",\"variables\":{\"filter\":{\"filterCriteria\":[{" \
                  "\"key\":\"userId\",\"operator\":\"IN\",\"value\":users_id}," \
                  "{\"key\":\"activityDate\",\"operator\":\"RANGE\",\"value\":[\"start_date\"," \
                  "\"end_date\"]},{\"key\":\"entityType\",\"operator\":\"EQ\"," \
                  "\"value\":\"entityTypeValue\"},{\"key\":\"entityId\",\"operator\":\"EQ\",\"value\":orderId}]}}," \
                  "\"query\":\"query downloadAuditLog($filter:Filter){\\n path:downloadAuditLog(" \
                  "filter:$filter)\\n}\\n\"} "
        payload = payload.replace('users_id', str(users_id))
        payload = payload.replace('start_date', str(start_date))
        payload = payload.replace('end_date', str(end_date))
        payload = payload.replace('entityTypeValue', entityTypeValue)
        payload = payload.replace('orderId', str(orderId))
        self.logger("info","payload after replacement: {payload}".format(payload=payload))
        headers = {
            'authorization': str(token),
            'x-resourceid': str(resource_query_data[0][0]),
            'x-organizationid': str(organization_id),
            'x-applicationid': str(application_id),
            'content-type': "application/json",
            'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
        }
        self.logger("info","Token used here:: {req_token}".format(req_token=token))
        self.logger("info","Request headers : {headers}".format(headers=headers))
        #self.logger("info","Request payload : {body}".format(body=payload))
        self.logger("info",endpoint_url)
        response = requests.post(endpoint_url, headers=headers, data=payload, verify=True, proxies=proxies)
        response_data = response.text
        response_data = json.loads(response_data)
        self.logger("info","\nAPI Response: {} \n".format(response_data))
        if "errors" in response_data:
            raise AssertionError("Generate Data for Delivery Alerts is Failed!!")
        else:
            self.logger("info","Generate Data for Delivery Alerts is Completed!!")
        file_name = str(response_data['data']['path'])
        file_url = str(response_data['data']['path'])
        self.logger("info",file_url)
        self.logger("info",file_name)
        self.logger("info",file_name.split("/")[-1])
        file_data = {'file_url': file_url, 'file_name': file_name}
        return file_data
        # except Exception as e:
        #     raise AssertionError("Audit File Download API is failed!!")

    def get_audit_log_users(self, **kwargs):
        try:
            token = self.builtlib.get_variable_value('${token}')
            endpoint_url = self.builtlib.get_variable_value('${endpoint_url}')
            proxies = os.environ.get('proxies')
            # If token is empty
            if token is None or token == '' or endpoint_url is None:
                self.generate_token()
                token = self.builtlib.get_variable_value('${token}')
                endpoint_url = self.builtlib.get_variable_value('${endpoint_url}')
            organization_id = kwargs.get('organization_id')
            advertiser_id = kwargs.get('advertiser_id')
            resource_id = kwargs.get('resource_id')
            application_id = kwargs.get('application_id')

            if organization_id and resource_id:
                resource_query = 'select resourceId from  common.RESOURCE where organizationId = {organization_id} and resourceValue = {resource_value};'.format(
                    organization_id=organization_id, resource_value=advertiser_id)
                resource_query_data = self.db.execute_query(db_query=resource_query)
                self.logger("info","Resource query : {resource_query} ".format(resource_query=resource_query))
                self.logger("info","Resource id from query is :: {res_id}".format(res_id=resource_query_data))
            else:
                raise Exception("advertiser or publisher for resourceId calculation is missing in parameters")
            payload = "{\"operationName\":\"getAuditLogUsers\",\"variables\":{},\"query\":\"query getAuditLogUsers{" \
                      "\\n getAuditLogUsers{\\n userId\\n name\\n __typename\\n}\\n}\\n\"} "
            headers = {
                'authorization': str(token),
                'x-resourceid':str(resource_id),
                'x-organizationid': str(organization_id),
                'x-applicationid': str(application_id),
                'content-type': "application/json",
                'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
            }
            self.logger("info","Token used here:: {req_token}".format(req_token=token))
            self.logger("info","Request headers : {headers}".format(headers=headers))
            #self.logger("info","Request payload : {body}".format(body=payload))
            self.logger("info",endpoint_url)
            response = requests.post(endpoint_url, headers=headers, data=payload, verify=True, proxies=proxies)
            response_data = response.text
            response_data = json.loads(response_data)
            self.logger("info","\nAPI Response: {} \n".format(response_data))
            if "errors" in response_data:
                raise AssertionError("Get Audit Log Users activity is Failed!!")
            else:
                self.logger("info","Get Audit Log Users Activity is Completed!!")
            users_data = response_data['data']['getAuditLogUsers']
            users_id_list = list()
            for user_id in users_data:
                users_id_list.append(user_id.get('userId'))
            self.logger("info",users_id_list)
            users_id_list = ','.join(str(e) for e in users_id_list)
            users_id_list = "[" + users_id_list + "]"
            self.logger("info",users_id_list)
            return users_id_list
        except:
            raise AssertionError("Get Audit Log Users activity is Failed!!")

    def add_days_to_date(self, **kwargs):
        # try:
        startDate = kwargs.get('start_date', False)
        endDate = kwargs.get('end_date')
        days = ""
        if startDate:
            if 'day' in str(startDate).lower():
                if ' ' in startDate:
                    days = str(startDate).split(' ')[0]
                elif 'days' in str(startDate).lower():
                    days = str(startDate).replace("days", "").strip()
                elif 'day' in str(startDate).lower():
                    days = str(startDate).replace("day", "").strip()

                startDate = datetime.today()
                tempDate = "" + str(startDate.year) + "" "-" "" + str(startDate.month) + "" "-" "" + \
                           str(startDate.day) + "" " " "" + str(startDate.hour) + "" ":" "" + str(
                    startDate.minute) + ""
                date_select = datetime.strptime(tempDate, '%Y-%m-%d %H:%M')
                date_select = date_select + timedelta(days=int(days))
            else:
                if ' ' in str(startDate):
                    startDate = str(startDate).split(' ')[0]
                date_select = datetime.strptime(startDate, '%Y-%m-%d %H:%M')

            self.logger("info","startDate: {}".format(date_select))
            return date_select
        elif endDate:
            if 'day' in str(endDate).lower():
                if ' ' in endDate:
                    days = str(endDate).split(' ')[0]
                elif 'days' in str(endDate).lower():
                    days = str(endDate).replace("days", "").strip()
                elif 'day' in str(endDate).lower():
                    days = str(endDate).replace("day", "").strip()
                endDate = datetime.today()
                tempDate = "" + str(endDate.year) + "" "-" "" + str(endDate.month) + "" "-" "" + \
                           str(endDate.day) + "" " " "" + str(23) + "" ":" "" + str(59) + ""
                date_select = datetime.strptime(tempDate, '%Y-%m-%d %H:%M')
                date_select = date_select + timedelta(days=int(days))
                self.logger("info","inside if: " + str(date_select))
            else:
                self.logger("info","Inside Else: ")
                date_select = datetime.strptime(endDate, '%Y-%m-%d %H:%M')
                self.logger("info","Inside Else: " + str(date_select))
            self.logger("info","endDate: {}".format(date_select))
            return date_select
        #
        # except Exception as e:
        #     raise AssertionError("Add Days to Date Activity is Failed!!")

    def send_user_invitation_email(self, **kwargs):
        try:
            user_email_address = kwargs.get('user_email_address')
            user_role = kwargs.get('user_role')
            org_id = kwargs.get('org_id', '10000')
            proxies = os.environ.get('proxies')

            self.logger("info",user_email_address,show_logs=True)
            if not (user_email_address and user_role):
                raise Exception("No username/user role passed, please pass a valid username and/or role")

            token = self.builtlib.get_variable_value('${token}')
            endpoint_url = self.builtlib.get_variable_value('${endpoint_url}')

            if token is None or token == '' or endpoint_url is None:
                self.generate_token()
                token = self.builtlib.get_variable_value('${token}')
                endpoint_url = self.builtlib.get_variable_value('${endpoint_url}')

            headers = {
                'authority': endpoint_url,
                'x-resourceid': "null",
                'accept': "*/*",
                'x-applicationid': "1",
                'authorization': token,
                'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
                'content-type': "application/json",
                'sec-gpc': "1",
                'origin': "https://account-manager-dev.deepintent.com",
                'sec-fetch-site': "same-site",
                'sec-fetch-mode': "cors",
                'sec-fetch-dest': "empty",
                'referer': "https://account-manager-dev.deepintent.com/",
                'accept-language': "en-GB,en-US;q=0.9,en;q=0.8",
                'x-organizationId': str(org_id)
            }

            payload = "{\"query\":\"mutation addUsersToOrg($organizationUserInput: OrganizationUserCreateInput!, $sendEmail: Boolean) " \
                      "{  addUsersToOrganization(organizationUserInput: $organizationUserInput, sendEmail: $sendEmail) {    " \
                      "organizationId    userId    user {      userId      email      emailVerified    }  }}\",\"variables\":" \
                      "{\"organizationUserInput\":{\"users\":[{\"email\":\"email_address\",\"role\":\"user_role\"}]}," \
                      "\"sendEmail\":true},\"operationName\":\"addUsersToOrg\"}"

            payload = payload.replace("email_address", str(user_email_address))
            payload = payload.replace("user_role", str(user_role).upper())
            self.logger("info",payload,show_logs=True)
            response = requests.post(endpoint_url, headers=headers, data=payload, verify=True, proxies=proxies)
            new = json.loads(response.content)
            self.logger("info", response.content, show_logs=True)

            if "errors" in new:
                raise Exception("API request failed. Got error in the response.!!!")

            else:
                self.logger("info",f"User with email {str(user_email_address)} has been added to org {str(org_id)}")

            self.logger("info","send_user_invitation_email function successful")

            return new

        except:
            tb = traceback.format_exc()
            self.raise_exception(tb)

        finally:
            self.logger("info","send_user_invitation function completed")

    def add_user(self, **kwargs):
        try:
            user_name = kwargs.get('user_name', 'test')
            user_password = kwargs.get('user_password')
            isExternal=kwargs.get('isExternal',False)
            is_non_platform=kwargs.get('is_non_platform_user',False)
            if kwargs.get('user_password', None) is not None:
                password_ = kwargs.get('user_password')
                user_password = os.environ.get(password_)
            user_role = kwargs.get('user_role')
            org_id = kwargs.get('org_id', '10000')
            proxies = os.environ.get('proxies')

            if not (user_name and user_role):
                raise Exception("No username/role passed, please pass a valid username and/or role")

            user_name = str(user_name) + '-' + str(user_role).lower()
            random_text = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
            user_name = user_name + '_' + str(random_text).lower()

            # Generate email address
            email_address, sid_token = self.email.return_random_email(user_name=user_name)
            if is_non_platform:
                return email_address, sid_token

            # Send invitation mail
            self.send_user_invitation_email(user_email_address=email_address, user_role=user_role, org_id=org_id)

            time.sleep(8)

            # Get Sign Up token
            signup_token = self.get_user_signup_token(email_address=email_address, sid_token=sid_token)

            self.logger("info",f"Generated email address: {str(email_address)}\nGenerated Sign Up token: {str(signup_token)}")

            endpoint_url = self.builtlib.get_variable_value('${endpoint_url}')

            if endpoint_url is None:
                self.generate_token()
                endpoint_url = self.builtlib.get_variable_value('${endpoint_url}')

            auth_token = 'Bearer {}'.format(str(signup_token).strip())

            headers = {'authority': 'gateway-service-dev.deepintent.com', 'X-OrganizationId': 'null', 'authorization': auth_token,
                       'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
                       'Content-Type': 'application/json', 'x-resource': 'advertiserId:', 'sec-gpc': '1', 'origin': 'https://sso-dev.deepintent.com',
                       'sec-fetch-site': 'same-site', 'sec-fetch-mode': 'cors', 'sec-fetch-dest': 'empty', 'referer': 'https://sso-dev.deepintent.com/',
                       'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'}

            data = "{\"query\":\"mutation signUpUser($userOnboardInput: OnboardUserInput!, $tokenType: TokenType!) {\\n\\tuserOnboard(userOnboardInput: $userOnboardInput, tokenType: $tokenType) {\\n\\t\\tuserId\\n\\t}\\n}\",\"variables\":{\"userOnboardInput\":{\"password\":\"user_password\",\"name\":\"user_name\"},\"tokenType\":\"SIGN_UP_TOKEN\"},\"operationName\":\"signUpUser\"}"
            if isExternal:
                data = "{\"query\":\"mutation signUpUser($userOnboardInput: OnboardUserInput!, $tokenType: TokenType!) {\\n\\tuserOnboard(userOnboardInput: $userOnboardInput, tokenType: $tokenType) {\\n\\t\\tuserId\\n\\t}\\n}\",\"variables\":{\"userOnboardInput\":{\"password\":\"user_password\",\"name\":\"user_name\"},\"isExternal\":true,\"tokenType\":\"SIGN_UP_TOKEN\"},\"operationName\":\"signUpUser\"}"
            data = data.replace('user_name', str(user_name))
            data = data.replace('user_password', str(user_password))

            self.logger("info",data)

            response = requests.post(endpoint_url, headers=headers, data=data, verify=True, proxies=proxies)
            self.logger("info",response.content)
            new = json.loads(response.content)

            if 'errors' in new:
                raise Exception("API request failed for add user. Got error in the response.!!!")

            user_count_query = f"select count(userId) from common.ORGANIZATION_USER where organizationId={str(org_id)};"
            user_count_data = self.db.execute_query(db_query=user_count_query)

            user_dict = {}

            user_dict.update({"userId": new['data']['userOnboard']['userId'], "email": str(email_address), 'userCount': user_count_data[0][0],"password": str(user_password),"sid_token":sid_token})

            self.logger("info",f"Added {str(user_count_data[0][0])} user(s) to org {str(org_id)}")

            return user_dict

        except:
            self.logger("info","add_user function failed")
            tb = traceback.format_exc()
            self.raise_exception(tb)

        finally:
            self.logger("info","add_user function completed")

    def add_user_without_signup_token(self, **kwargs):
        try:
            user_name = kwargs.get('user_name', 'test')
            user_password = kwargs.get('user_password')
            user_role = kwargs.get('user_role')
            org_id = kwargs.get('org_id', '10000')

            if not (user_name and user_role):
                raise Exception("No username/role passed, please pass a valid username and/or role")

            user_name = str(user_name)
            random_text = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
            user_name = user_name + '_' + str(random_text).lower()

            # Generate email address
            email_address, sid_token = self.email.return_random_email(user_name=user_name)

            # Get Sign Up token
            #signup_token = self.get_user_signup_token(email_address=email_address, sid_token=sid_token)

            self.db.execute_query(db_query="UPDATE common.`USER` SET emailVerified = 1 WHERE email = '{}'".format(email_address))
            self.db.execute_query(
                db_query="UPDATE common.`USER` SET password = '{}' WHERE email = '{}'".format(os.environ.get("encrypted_password_for_reset"),email_address))
            self.db.execute_query(
                db_query="UPDATE common.`USER` SET status = 'ENABLED' WHERE email = '{}'".format(email_address))
            self.db.execute_query(
                db_query="UPDATE common.`USER` SET name = '{}' WHERE email = '{}'".format(str(email_address).split('@')[0],email_address))

            user_dict = {}
            user_dict.update({"email": str(email_address)})

            return user_dict

        except:
            self.logger("info","add_user_without_signup_token function failed")
            tb = traceback.format_exc()
            self.raise_exception(tb)

        finally:
            self.logger("info","add_user_without_signup_token function completed")

    def get_executed_time(self, **kwargs):
        try:
            start_date = kwargs.get('start_date')

            # Get End Time
            end_time = Date(datetime.now()).convert('datetime')

            # Get Difference
            diff = end_time - start_date
            elapsed_time = int((diff.seconds * 1000) + (diff.microseconds / 1000))

            self.logger("info",f"Test Case Execution Time captured ({str(elapsed_time) + ' ms'})")

            return str(elapsed_time) + ' ms'

        except:
            tb = traceback.format_exc()
            self.raise_exception(tb)

    def log_entries_to_db(self, **kwargs):
        try:
            # Get Exception Message
            if kwargs.get('exception_message'):
                kwargs.update({'status': 'FAILED'})
                kwargs.update({'message': kwargs.get('exception_message')})
            else:
                kwargs.update({'status': 'PASSED'})

            # Get Test Case Name
            test_name = self.builtlib.get_variable_value('${test_name}')
            kwargs.update({'test_name': test_name})

            # Get Test Case System (UI/API)
            if str(kwargs['system']).lower() == 'ui':
                test_case_type = 'UI'
            elif str(kwargs['system']).lower() == 'api':
                test_case_type = 'API'

            # Get Test Case timestamp
            kwargs.update(({'timestamp': datetime.now().strftime("%Y-%m-%d")}))

            # Inserting test run record
            query = "INSERT INTO qa.PLANNER_MONITORING (test_name,execution_time,status, pp_section,rule, message,`system`,date, type) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}');".format(
                kwargs.get('test_name'), kwargs.get('executed_time'), kwargs.get('status'), kwargs.get('pp_section'),
                kwargs.get('rule'), kwargs.get('message'), test_case_type, kwargs.get('timestamp'), kwargs.get('type'))

            db_host_prod = 'mysql1-prod-useast.deepintent.com'
            db_user_prod = 'automation'
            db_password_prod = 'ienHWbrYhrDF'
            db_name_prod = 'bidder'
            db_port_prod = 3306

            self.planner_data.execute_query(db_host=db_host_prod,
                                       db_user=db_user_prod,
                                       db_password=db_password_prod,
                                       db_name=db_name_prod,
                                       db_port=db_port_prod,db_query=query)

            self.logger("info","log_entries_to_db function successful")

        except:
            self.logger("info","log_entries_to_db function failed")
            tb = traceback.format_exc()
            self.raise_exception(tb)

        finally:
            self.logger("info","log_entries_to_db function completed")

    def print_request_curl(self, req):
        """
        Usage :
            req_curl = self.print_request_curl(response.request)
            self.logger("info","req_curl = {req_curl}".format(req_curl=req_curl))
        """
        command = "curl --request {method}\ \n--header {headers}\ \n--data '{data}'\ \n--url '{uri}'"
        method = req.method
        uri = req.url
        data = req.body
        headers = ['"{0}: {1}"'.format(k, v) for k, v in req.headers.items()]
        headers = " --header ".join(headers)
        return command.format(method=method, headers=headers, data=data, uri=uri)

    def get_user_signup_token(self, **kwargs):
        try:
            # email_address = kwargs.get('email_address')
            # user_name, domain = email_address.split('@')
            # temp_mail_endpoint_to_get_message_id = f"https://www.1secmail.com/api/v1/?action=getMessages&login={str(user_name)}&domain={str(domain)}"
            # self.logger("info",temp_mail_endpoint_to_get_message_id)
            # time.sleep(3)
            # response = requests.post(temp_mail_endpoint_to_get_message_id)
            # response_text = ast.literal_eval(response.text)
            # user_id = ""
            #
            # for content in response_text:
            #     user_id = content['id']
            #
            # # Get Message Body and Sign Up token
            # temp_mail_endpoint_to_get_message_body = f"https://www.1secmail.com/api/v1/?action=readMessage&login={str(user_name)}&domain={str(domain)}&id={str(user_id)}"
            # response = requests.post(temp_mail_endpoint_to_get_message_body)
            # response_json = json.loads(response.text)
            # message_body = response_json['body']
            #
            # files = re.findall("href=[\"\'](.*?)[\"\']", message_body)
            # for em in files:
            #     if 'https://sso-dev.deepintent.com/#/invite/?' in em:
            #         token_string = em
            #         signup_token = token_string[token_string.find('=') + 1:]
            #         self.logger("info","Sign Up token {}".format(signup_token))
            #         return signup_token
            #
            # raise Exception("Sign Up token not received on email")

            sid_token = kwargs.get('sid_token')
            time.sleep(5)

            check_email_url = f'https://api.guerrillamail.com/ajax.php?f=check_email&sid_token={str(sid_token)}&seq=0'
            check_email_response = requests.get(check_email_url)
            check_email_response = json.loads(check_email_response.text)

            for email in check_email_response['list']:
                if email['mail_from'] == 'admin@deepintent.com':
                    email_id = email['mail_id']

            fetch_email_url = f'https://api.guerrillamail.com/ajax.php?f=fetch_email&sid_token={str(sid_token)}&email_id={str(email_id)}'
            fetch_email_response = requests.get(fetch_email_url)
            fetch_email_response = json.loads(fetch_email_response.text)
            message_body = fetch_email_response['mail_body']

            files = re.findall("href=[\"\'](.*?)[\"\']", message_body)
            for em in files:
                if 'https://sso-dev.deepintent.com/#/invite/?' in em:
                    token_string = em
                    signup_token = token_string[token_string.find('=') + 1:]
                    self.logger("info","Sign Up token {}".format(signup_token))
                    return signup_token

            raise Exception("Sign Up token not received on email")

        except:
            self.logger("info","get_user_signup_token function failed")
            tb = traceback.format_exc()
            self.raise_exception(tb)

        finally:
            self.logger("info","get_user_signup_token function completed")

    def get_mfa_otp_from_mail(self, **kwargs):
        try:
            # email_address = kwargs.get('email_address')
            # user_name, domain = email_address.split('@')
            # temp_mail_endpoint_to_get_message_id = f"https://www.1secmail.com/api/v1/?action=getMessages&login={str(user_name)}&domain={str(domain)}"
            #
            # response = requests.post(temp_mail_endpoint_to_get_message_id)
            # response_text = ast.literal_eval(response.text)
            #
            # temp_mail_endpoint_to_get_message_body = f"https://www.1secmail.com/api/v1/?action=readMessage&login={str(user_name)}&domain={str(domain)}&id={str(response_text[0]['id'])}"
            # self.logger("info",temp_mail_endpoint_to_get_message_body)
            # response = requests.post(temp_mail_endpoint_to_get_message_body)
            # response_json = json.loads(response.text)
            # self.logger("info",response_json)
            # message_body = response_json['body']
            # #self.logger("info","OTP : {}".format(message_body))
            # otp = re.findall('<h1 class="content-otp">(.*?)</h1>',message_body)
            # return otp[0]

            sid_token = kwargs.get('sid_token')
            time.sleep(5)

            cnt = 0
            cnt1 = 0
            check_email_url = f'https://api.guerrillamail.com/ajax.php?f=check_email&sid_token={str(sid_token)}&seq=0'
            while cnt < 2:
                while cnt1 < 2:
                    check_email_response = requests.get(check_email_url)
                    check_email_response = json.loads(check_email_response.text)
                    if len(check_email_response['list']) > 0:
                        break
                    cnt1 = cnt1 + 1
                email_id = check_email_response['list'][0]['mail_id']

                fetch_email_url = f'https://api.guerrillamail.com/ajax.php?f=fetch_email&sid_token={str(sid_token)}&email_id={str(email_id)}'
                fetch_email_response = requests.get(fetch_email_url)
                fetch_email_response = json.loads(fetch_email_response.text)
                message_body = fetch_email_response['mail_body']

                otp = re.findall(' <h1>(.*?)</h1>', message_body)
                if len(otp) >= 1:
                    break
                cnt = cnt + 1
            return otp[1]

        except:
            self.logger("info","get_mfa_otp_from_mail function failed")
            tb = traceback.format_exc()
            self.raise_exception(tb)

        finally:
            self.logger("info","get_mfa_otp_from_mail function completed")

    def get_magic_link_from_mail(self, **kwargs):
        try:
            # email_address = kwargs.get('email_address')
            # user_name, domain = email_address.split('@')
            # temp_mail_endpoint_to_get_message_id = f"https://www.1secmail.com/api/v1/?action=getMessages&login={str(user_name)}&domain={str(domain)}"
            #
            # response = requests.post(temp_mail_endpoint_to_get_message_id)
            # response_text = ast.literal_eval(response.text)
            #
            # temp_mail_endpoint_to_get_message_body = f"https://www.1secmail.com/api/v1/?action=readMessage&login={str(user_name)}&domain={str(domain)}&id={str(response_text[0]['id'])}"
            # self.logger("info",temp_mail_endpoint_to_get_message_body)
            # response = requests.post(temp_mail_endpoint_to_get_message_body)
            # response_json = json.loads(response.text)
            # self.logger("info",response_json)
            # message_body = response_json['body']
            # #self.logger("info","OTP : {}".format(message_body))
            # magic_link = re.findall('<a href="(.*?)" class="button" target="_blank">Login using Magic Link</a>',message_body)
            # self.logger("info","Magic Link : {}".format(magic_link))
            # return magic_link[0]

            sid_token = kwargs.get('sid_token')
            time.sleep(5)

            cnt = 0
            while cnt < 2:
                check_email_url = f'https://api.guerrillamail.com/ajax.php?f=check_email&sid_token={str(sid_token)}&seq=0'
                check_email_response = requests.get(check_email_url)
                check_email_response = json.loads(check_email_response.text)

                email_id = check_email_response['list'][0]['mail_id']

                fetch_email_url = f'https://api.guerrillamail.com/ajax.php?f=fetch_email&sid_token={str(sid_token)}&email_id={str(email_id)}'
                fetch_email_response = requests.get(fetch_email_url)
                fetch_email_response = json.loads(fetch_email_response.text)
                message_body = fetch_email_response['mail_body']
                magic_link = re.findall('<a href="(.*?)">Login using Magic Link</a>',
                                    message_body)
                if len(magic_link) > 0:
                    break
                cnt = cnt + 1
                self.logger("info","Magic Link : {}".format(magic_link))

            return magic_link[0]

        except:
            self.logger("info","get_magic_link_from_mail function failed")
            tb = traceback.format_exc()
            self.raise_exception(tb)

        finally:
            self.logger("info","get_magic_link_from_mail function completed")

    def get_qr_code_mail(self, **kwargs):
        try:

            sid_token = kwargs.get('sid_token')
            time.sleep(5)

            check_email_url = f'https://api.guerrillamail.com/ajax.php?f=check_email&sid_token={str(sid_token)}&seq=0'
            check_email_response = requests.get(check_email_url)
            check_email_response = json.loads(check_email_response.text)

            email_id = check_email_response['list'][0]['mail_id']

            img_url = []
            counter = 0
            while counter < 5:
                fetch_email_url = f'https://api.guerrillamail.com/ajax.php?f=fetch_email&sid_token={str(sid_token)}&email_id={str(email_id)}'
                fetch_email_response = requests.get(fetch_email_url)
                fetch_email_response = json.loads(fetch_email_response.text)
                message_body = fetch_email_response['mail_body']
                img_url = re.findall('<a href="(.*?)">Click here', message_body)
                self.logger("info",img_url, show_logs=True)
                if len(img_url) == 0:
                    break
                counter = counter+1

            return img_url[0]


            # email_address = kwargs.get('email_address')
            # user_name, domain = email_address.split('@')
            # temp_mail_endpoint_to_get_message_id = f"https://www.1secmail.com/api/v1/?action=getMessages&login={str(user_name)}&domain={str(domain)}"
            #
            # response = requests.post(temp_mail_endpoint_to_get_message_id)
            # response_text = ast.literal_eval(response.text)
            #
            # temp_mail_endpoint_to_get_message_body = f"https://www.1secmail.com/api/v1/?action=readMessage&login={str(user_name)}&domain={str(domain)}&id={str(response_text[0]['id'])}"
            # self.logger("info",temp_mail_endpoint_to_get_message_body)
            # response = requests.post(temp_mail_endpoint_to_get_message_body)
            # response_json = json.loads(response.text)
            # self.logger("info",response_json)
            # message_body = response_json['body']

        except:
            self.logger("info","get_qr_code_mail function failed")
            tb = traceback.format_exc()
            self.raise_exception(tb)

        finally:
            self.logger("info","get_qr_code_mail function completed")

    def convert_csv_strings_to_list(self, column_list):
        try:
            if not isinstance(column_list, list) and '[' == str(column_list)[0] and ']' == str(column_list)[-1]:
                column_list = ast.literal_eval(column_list)
            if isinstance(column_list, str) or isinstance(column_list, int):
                if isinstance(column_list, int):
                    column_list = str(column_list)
                column_list = [x.strip().title() for x in column_list.split(",") if len(x) > 0]
            return column_list
        except:
            self.logger("error","convert_csv_strings_to_list Function failed.")
            tb = traceback.format_exc()
            raise Exception(tb)
        finally:
            self.logger("info","hide_page_columns Function completed.")

    def convert_float_to_str_percent(self, val):
        """if val is 11.0(float), then convert to 11.00(str) else return as it is"""
        return str(val)+"0"*(2-len(str(round(val, 2)).split('.')[1]))+'%' if isinstance(val, float) else val

    def db_query_retry(self, db_query, result_count='no_count', retry_count=5, sleep_interval=2):
        """
        retry query after every 1 second until data is available if result_count is not set
        result_count = check if tuple count of query result is equal to result_count
        """
        try:
            # retry_count = 5
            query_result = self.db.execute_query(db_query=db_query)
            logger.info(f"-1_query_result = {query_result}")
            for i in range(0, int(retry_count)):
                if result_count == 'no_count' and len(query_result) > 0 and len(query_result[0]) > 0:
                    break
                elif result_count != 'no_count' and len(query_result) == int(result_count):
                    break
                else:
                    self.logger("info", f"retrying query {i}")
                    time.sleep(int(sleep_interval))
                    query_result = self.db.execute_query(db_query=db_query)
            logger.info(f"{i}_query_result last = {query_result}")
            return query_result

        except:
            self.logger("error",traceback.format_exc())
            self.logger("error","db_query_retry Failed")
            tb = traceback.format_exc()
            self.raise_exception(tb)
        finally:
            self.logger("info","db_query_retry Function Completed")

    def convert_db_data_to_data_dict(self, db_tuple, column_list):
        l1 = []
        self.logger("info",f"db_tuple = {db_tuple}")
        self.logger("info",f"column_list = {column_list}")
        if len(db_tuple) > 0:
            assert len(db_tuple[0]) == len(column_list), f"length of db_tuple columns and column_list should be same len(db_tuple[0])={len(db_tuple[0])} != len(column_list)({len(column_list)})"
            for item in db_tuple:
                l1.append(dict(zip(column_list, item)))
        return l1

    def logger(self,type=None,message=None, show_logs=False):
        try:
            if type is not None:
                type = str(type).lower()
            if show_logs:
                if message is not None:
                    if type == "info":
                        logger.info(message)
                    elif type == "error":
                        logger.error(message)
                    elif type is not None:
                        logger.info(message)
            elif message is not None:
                if type == "error":
                    logger.error(message)
        except Exception:
            pass

    def generate_jwt_token_for_signup(self, userId):
        try:
            user_id_reset_password = int(userId)
            secret = os.environ.get('reset_password_token_secret')
            token = jwt.encode(payload={
                "iss": "deepintent",
                "mfaEnabled": False,
                "elevatedUser": True,
                "tokenType": "SIGN_UP_TOKEN",
                "env": "development",
                "exp": (datetime.now() + timedelta(days=1)).timestamp(),
                "userId": user_id_reset_password
            }, key=secret, algorithm='HS256')
            logger.info("token "+str(token))
            self.store_token_in_redis(token)
            return token
        except Exception as e:
            logger.info("generate_jwt_token_for_reset_password failed")
            raise Exception(e)
        finally:
            logger.info("generate_jwt_token_for_reset_password completed")

    def store_token_in_redis(self,token):
        try:
            redis_port = os.environ.get('redis_port_password_store')
            redis_url = os.environ.get('redis_url')
            redis_master = os.environ.get('redis_master')
            redis_password = os.environ.get('redis_password')
            logger.info(redis_port)
            logger.info(redis_url)
            logger.info(redis_master)
            logger.info(redis_password)
            sentinel = Sentinel([
                (redis_url, redis_port)
            ])
            host, port = sentinel.discover_master(redis_master)

            redis_client = redis.StrictRedis(
                host=host,
                port=port,
                password=redis_password
            )
            logger.info("Redis Client")
            logger.info(redis_client)
            redis_client.json().set(token, '$', '1')
            logger.info(redis_client.json().get(token))
            redis_client.expireat(name=token, when=datetime.now() + timedelta(days=1))

        except Exception as e:
            logger.info("store_token_in_redis failed")
            raise Exception(e)
        finally:
            redis_client.close()
            logger.info("store_token_in_redis completed")

    def add_user_with_storing_token_in_redis(self, **kwargs):
        try:
            user_name = kwargs.get('user_name', 'test')
            user_password = kwargs.get('user_password')
            isExternal=kwargs.get('isExternal',False)
            is_non_platform=kwargs.get('is_non_platform_user',False)
            if kwargs.get('user_password', None) is not None:
                password_ = kwargs.get('user_password')
                user_password = os.environ.get(password_)
            user_role = kwargs.get('user_role')
            org_id = kwargs.get('org_id', '10000')
            proxies = os.environ.get('proxies')

            if not (user_name and user_role):
                raise Exception("No username/role passed, please pass a valid username and/or role")

            user_name = str(user_name) + '-' + str(user_role).lower()
            random_text = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
            user_name = user_name + '_' + str(random_text).lower()

            # Generate email address
            email_address, sid_token = self.email.return_random_email(user_name=user_name)
            if is_non_platform:
                return email_address, sid_token

            # Send invitation mail
            data = self.send_user_invitation_email(user_email_address=email_address, user_role=user_role, org_id=org_id)

            time.sleep(2)

            # Get Sign Up token
            signup_token = self.generate_jwt_token_for_signup(data['data']['addUsersToOrganization'][0]['userId'])

            self.logger("info",f"Generated email address: {str(email_address)}\nGenerated Sign Up token: {str(signup_token)}")

            endpoint_url = self.builtlib.get_variable_value('${endpoint_url}')

            if endpoint_url is None:
                self.generate_token()
                endpoint_url = self.builtlib.get_variable_value('${endpoint_url}')

            auth_token = 'Bearer {}'.format(str(signup_token).strip())

            headers = {'authority': 'gateway-service-dev.deepintent.com', 'X-OrganizationId': 'null', 'authorization': auth_token,
                       'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
                       'Content-Type': 'application/json', 'x-resource': 'advertiserId:', 'sec-gpc': '1', 'origin': 'https://sso-dev.deepintent.com',
                       'sec-fetch-site': 'same-site', 'sec-fetch-mode': 'cors', 'sec-fetch-dest': 'empty', 'referer': 'https://sso-dev.deepintent.com/',
                       'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'}

            data = "{\"query\":\"mutation signUpUser($userOnboardInput: OnboardUserInput!, $tokenType: TokenType!) {\\n\\tuserOnboard(userOnboardInput: $userOnboardInput, tokenType: $tokenType) {\\n\\t\\tuserId\\n\\t}\\n}\",\"variables\":{\"userOnboardInput\":{\"password\":\"user_password\",\"name\":\"user_name\"},\"tokenType\":\"SIGN_UP_TOKEN\"},\"operationName\":\"signUpUser\"}"
            if isExternal:
                data = "{\"query\":\"mutation signUpUser($userOnboardInput: OnboardUserInput!, $tokenType: TokenType!) {\\n\\tuserOnboard(userOnboardInput: $userOnboardInput, tokenType: $tokenType) {\\n\\t\\tuserId\\n\\t}\\n}\",\"variables\":{\"userOnboardInput\":{\"password\":\"user_password\",\"name\":\"user_name\"},\"isExternal\":true,\"tokenType\":\"SIGN_UP_TOKEN\"},\"operationName\":\"signUpUser\"}"
            data = data.replace('user_name', str(user_name))
            data = data.replace('user_password', str(user_password))

            self.logger("info",data)

            response = requests.post(endpoint_url, headers=headers, data=data, verify=True, proxies=proxies)
            if response.status_code != 200:
                # Get Sign Up token
                signup_token = self.generate_jwt_token_for_signup(data['data']['addUsersToOrganization'][0]['userId'])
                headers['authorization'] = 'Bearer {}'.format(str(signup_token).strip())
                response = requests.post(endpoint_url, headers=headers, data=data, verify=True, proxies=proxies)


            self.logger("info",response.content)
            new = json.loads(response.content)

            if 'errors' in new:
                raise Exception("API request failed for add user. Got error in the response.!!!")

            user_count_query = f"select count(userId) from common.ORGANIZATION_USER where organizationId={str(org_id)};"
            user_count_data = self.db.execute_query(db_query=user_count_query)

            user_dict = {}

            user_dict.update({"userId": new['data']['userOnboard']['userId'], "email": str(email_address), 'userCount': user_count_data[0][0],"password": str(user_password),"sid_token":sid_token,"sign_up_token":signup_token})

            self.logger("info",f"Added {str(user_count_data[0][0])} user(s) to org {str(org_id)}")

            return user_dict

        except:
            self.logger("info","add_user function failed")
            tb = traceback.format_exc()
            self.raise_exception(tb)

        finally:
            self.logger("info","add_user function completed")

    def create_creative_api(self, **kwargs):
        try:
            # Input Parameters
            organizationId = kwargs.get('organizationId', 10000)
            resourceValue = kwargs.get('advertiser_id', 10001)
            assetTypeId = kwargs.get('assetTypeId')
            campaign_id = kwargs.get('campaign_id')
            height = kwargs.get('height')
            width = kwargs.get('width')
            random_number = ''.join(random.choices(string.digits, k=5))

            if organizationId is None or resourceValue is None:
                raise Exception("organization_id OR advertiser_id OR campaign_id missing in the input parameters")

            resource_query = 'select resourceId from  common.RESOURCE where organizationId = {organization_id} and ' \
                             'resourceValue = {resource_value};'.format(organization_id=organizationId,
                                                                        resource_value=resourceValue)
            resource_query_data = self.db.execute_query(db_query=resource_query)
            logger.info("Resource query : {resource_query} ".format(resource_query=resource_query))
            logger.info("Resource id from query is :: {res_id}".format(res_id=resource_query_data))
            resourceId = resource_query_data[0][0]

            get_asset_id_query = """SELECT cfat.assetTypeId, cf.name, at2.displayName  
            FROM CREATIVE_FORMAT_ASSET_TYPE cfat 
            JOIN ASSET_TYPE at2 ON cfat.assetTypeId = at2.assetTypeId 
            JOIN CREATIVE_FORMAT cf ON cfat.creativeFormatId = cf.formatId where cf.formatId =1 and cfat.assetTypeId ={assetTypeId}
            """.format(assetTypeId=assetTypeId)
            get_asset_id_query_data = self.db.execute_query(db_query=get_asset_id_query)

            assetTypeId = get_asset_id_query_data[0][0]
            nameBanner = get_asset_id_query_data[0][1]

            if assetTypeId is None:
                assetTypeId = "null"

            # assetTypeId, name, displayName
            # 1	BANNER	Image
            # 5	BANNER	HTML/Ad Tag
            # 7	BANNER	Rich Media (File Upload)

            payload = ('{\"operationName\":\"createCreative\",\"variables\":{\"creative\":{\"format\":\"name_banner_format\",' \
                       '\"assetsMapped\":[{\"assetId\":null,\"asset\":\"</>\",\"assetTypeId\":assetType_id,\"assetSubTypeId\":null,' \
                       '\"required\":true,\"height\":height_size,\"width\":width_size}],\"name\":\"BannerCreativeName\",' \
                       '\"landingUrl\":\"\",\"secure\":true,\"isCTVCertified\":null,\"startDate\":null,\"endDate\":null,\"status\":\"ENABLED\",' \
                       '\"creativeTrackers\":[],\"vendor\":null,\"adChoices\":\"N\",\"isDOOHCreative\":false,\"adChoicePosition\":\"TOP_RIGHT\"},' \
                       '\"file\":[],\"fileV2\":true},\"query\":\"mutation createCreative($file: [Upload], $creative: CreativeInput) ' \
                       '{\\n  createCreative(file: $file, creativeInput: $creative) {\\n    creativeId\\n    name\\n    landingUrl\\n    secure\\n    status\\n    adSize {\\n      displayValue\\n      __typename\\n    }\\n    assets {\\n      properties\\n      asset\\n      __typename\\n    }\\n    isCTVCertified\\n    isDOOHCreative\\n    __typename\\n  }\\n}\\n"}')

            payload = payload.replace('assetType_id', str(assetTypeId))
            payload = payload.replace('name_banner_format', str(nameBanner))
            payload = payload.replace('height_size', str(height))
            payload = payload.replace('width_size', str(width))
            new_name = "QA_Banner_" + random_number
            payload = payload.replace('BannerCreativeName', str(new_name))

            headers = {
                "x-resourceid": str(resourceId),
                'x-organizationid': str(organizationId),
                'x-applicationid': "2"
            }

            logger.info("Request headers : {headers}".format(headers=headers))
            logger.info("Request payload : {body}".format(body=payload))

            dict = {}
            dict.update({'payload': payload})
            dict.update({'headers': headers})
            response = self.get_api_response(dict)
            logger.info("API response : {api_resp}".format(api_resp=str(response.text)))

            response_data = response.text
            response_data = json.loads(response_data)

            if "errors" in response_data:
                raise Exception("API request failed. Got error in the response.!!!")
            else:
                logger.info(response_data)

            creative_name = response_data['data']['createCreative']['name']

            some_ui_text = "UI Tooltip text"
            som_db_text = "DB Txet"

            if str(some_ui_text) != srt(som_db_text):
                raise Expection("Names don't match")

            return creative_name

        except Exception as e:
            print(e.args)
            logger.info("Creative Creation Failed")
            raise Exception(e)

    def raise_exception(self,tb):
        raise Exception(tb)

if __name__ == '__main__':
    generate_token_automation()