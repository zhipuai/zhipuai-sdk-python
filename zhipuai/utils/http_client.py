# -*- coding:utf-8 -*-
import json
import logging

import requests
import aiohttp

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json; charset=UTF-8",
}


def post(api_url, token, params, timeout):
    try:
        headers.update({"Authorization": token})
        resp = requests.post(
            url=api_url, data=json.dumps(params), headers=headers, timeout=timeout
        )
        if requests.codes.ok != resp.status_code:
            raise Exception("响应异常：" + resp.content)
        return json.loads(resp.text)
    except Exception as e:
        logging.exception("请求异常", e)




async def apost(api_url, token, params, timeout):
    try:
        headers.update({"Authorization": token})
        async with aiohttp.ClientSession() as session:
            async with session.post(
                url=api_url, data=json.dumps(params), headers=headers, timeout=timeout
            ) as resp:
                if not resp.ok:
                    raise Exception("响应异常：" + await resp.text())
                return json.loads(await resp.text())
    except Exception as e:
        logging.exception("请求异常", e)


def stream(api_url, token, params, timeout):
    try:
        resp = requests.post(
            api_url,
            stream=True,
            headers={"Authorization": token},
            json=params,
            timeout=timeout,
        )
        if requests.codes.ok != resp.status_code:
            raise Exception("请求异常")
        return resp
    except Exception as e:
        logging.exception("请求异常", e)


def get(api_url, token, timeout):
    try:
        headers.update({"Authorization": token})
        resp = requests.get(api_url, headers=headers, timeout=timeout)
        if requests.codes.ok != resp.status_code:
            raise Exception("响应异常：" + resp.content)
        return json.loads(resp.text)
    except Exception as e:
        logging.exception("请求异常", e)
