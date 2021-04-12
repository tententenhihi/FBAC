import re

from requests import request


class FakeMail:

    def email(self):
        url = 'https://www.fakemail.net/index/index'

        headers = {'Accept': 'application/json, text/javascript, */*; q=0.01',
                   'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
                   'Host': 'www.fakemail.net', 'Connection': 'Keep-Alive', 'Referer': 'https://www.fakemail.net/',
                   'X-Requested-With': 'XMLHttpRequest'}

        try:
            response = request("GET", url, headers=headers, timeout=30)

            if response.status_code == 200:

                if ('email') in response.text:

                    try:
                        pattern = re.compile("{\"email\":\"(.*)\",")
                        search = pattern.search(response.text)
                        email = search.group(1)

                        return {'status': 'success', 'email': email,
                                'message': 'Email fetched successfully'}
                    except:

                        return {'status': 'error', 'message': 'Message received but unable to find Code'}
                else:

                    return {'status': 'error', 'message': 'Email id not found'}

            else:
                return {'status': 'error', 'message': '401 Unauthorized'}

        except:
            return {'status': 'error', 'message': 'Connection error'}

    def messages(self, email):
        url = 'https://www.fakemail.net/index/refresh'

        cookies = {'TMA': email}
        headers = {'Accept': 'application/json, text/javascript, */*; q=0.01',
                   'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
                   'Host': 'www.fakemail.net', 'Connection': 'Keep-Alive', 'Referer': 'https://www.fakemail.net/',
                   'X-Requested-With': 'XMLHttpRequest'}

        try:
            response = request("GET", url, headers=headers, cookies=cookies, timeout=30)

            if response.status_code == 200:

                if ('Facebook') in response.text:

                    try:
                        pattern = re.compile("FB-(\d+)")
                        search = pattern.search(response.text)
                        otp = search.group(1)

                        return {'status': 'success', 'otp': otp,
                                'message': 'OTP fetched successfully'}
                    except:

                        return {'status': 'error', 'message': 'Message received but unable to find Code'}
                else:

                    return {'status': 'error', 'message': 'Message not received from Facebook'}

            else:
                return {'status': 'error', 'message': '401 Unauthorized'}

        except:
            return {'status': 'error', 'message': 'Connection error'}
