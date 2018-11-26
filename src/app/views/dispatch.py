from django import views


class DispatchView(views.View):

    def get_http_handler(self, method):
        return dict(
            put=self.put if hasattr(self, 'put') else self.http_method_not_allowed,
            patch=self.patch if hasattr(self, 'patch') else self.http_method_not_allowed,
            delete=self.delete if hasattr(self, 'delete') else self.http_method_not_allowed,
        ).get(method, None)

    def dispatch(self, request, *args, **kwargs):
        http_method = request.POST.get('http_method', '')
        handler = self.get_http_handler(http_method)

        if not handler:
            return super().dispatch(request, *args, **kwargs)

        return handler(request, *args, **kwargs)
