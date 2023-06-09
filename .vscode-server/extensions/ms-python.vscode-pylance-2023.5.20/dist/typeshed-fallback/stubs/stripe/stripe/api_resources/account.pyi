from _typeshed import Incomplete

from stripe import oauth as oauth
from stripe.api_resources.abstract import (
    CreateableAPIResource as CreateableAPIResource,
    DeletableAPIResource as DeletableAPIResource,
    ListableAPIResource as ListableAPIResource,
    UpdateableAPIResource as UpdateableAPIResource,
    custom_method as custom_method,
    nested_resource_class_methods as nested_resource_class_methods,
)

class Account(CreateableAPIResource, DeletableAPIResource, ListableAPIResource):
    OBJECT_NAME: str
    def reject(self, idempotency_key: str | None = None, **params): ...
    @classmethod
    def retrieve(cls, id: Incomplete | None = None, api_key: Incomplete | None = None, **params): ...
    @classmethod
    def modify(cls, id: Incomplete | None = None, **params): ...
    def instance_url(self): ...
    def persons(self, idempotency_key: str | None = None, **params): ...
    def deauthorize(self, **params): ...
    def serialize(self, previous): ...
    @classmethod
    def capabilitys_url(cls, id, nested_id=None): ...
    @classmethod
    def capabilitys_request(
        cls, method, url, api_key=None, idempotency_key=None, stripe_version=None, stripe_account=None, **params
    ): ...
    @classmethod
    def retrieve_capability(cls, id, nested_id, **params): ...
    @classmethod
    def modify_capability(cls, id, nested_id, **params): ...
    @classmethod
    def list_capabilities(cls, id, **params): ...
    @classmethod
    def external_accounts_url(cls, id, nested_id=None): ...
    @classmethod
    def external_accounts_request(
        cls, method, url, api_key=None, idempotency_key=None, stripe_version=None, stripe_account=None, **params
    ): ...
    @classmethod
    def create_external_account(cls, id, **params): ...
    @classmethod
    def retrieve_external_account(cls, id, nested_id, **params): ...
    @classmethod
    def modify_external_account(cls, id, nested_id, **params): ...
    @classmethod
    def delete_external_account(cls, id, nested_id, **params): ...
    @classmethod
    def list_external_accounts(cls, id, **params): ...
    @classmethod
    def login_links_url(cls, id, nested_id=None): ...
    @classmethod
    def login_links_request(
        cls, method, url, api_key=None, idempotency_key=None, stripe_version=None, stripe_account=None, **params
    ): ...
    @classmethod
    def create_login_link(cls, id, **params): ...
    @classmethod
    def persons_url(cls, id, nested_id=None): ...
    @classmethod
    def persons_request(
        cls, method, url, api_key=None, idempotency_key=None, stripe_version=None, stripe_account=None, **params
    ): ...
    @classmethod
    def create_person(cls, id, **params): ...
    @classmethod
    def retrieve_person(cls, id, nested_id, **params): ...
    @classmethod
    def modify_person(cls, id, nested_id, **params): ...
    @classmethod
    def delete_person(cls, id, nested_id, **params): ...
    @classmethod
    def list_persons(cls, id, **params): ...
