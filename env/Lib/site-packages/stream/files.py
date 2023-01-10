class Files:
    def __init__(self, client, token):
        self.client = client
        self.token = token

    def upload(self, url, name, user_id, content_type=None):
        return self.client.upload_file(f"files/", url, name, user_id, content_type)

    def delete(self, user_id, data=None, get_or_create=False):
        payload = dict(id=user_id, data=data)
        return self.client.post(
            "user/",
            service_name="api",
            signature=self.token,
            data=payload,
            params={"get_or_create": get_or_create},
        )
