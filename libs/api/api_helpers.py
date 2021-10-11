from flask import request


def get(parameter):

    return request.args.get(parameter)
