# -*- coding: utf-8 -*-
"""Utilities for generating Android device information."""

import random
from typing import Dict, List, Optional

from . import config


class DeviceGenerator:
    """Simple generator for Android device details."""

    # Mapping of common device models to manufacturers
    DEFAULT_MODELS = {
        "SM-G991B": "samsung",
        "Pixel 6": "google",
        "Mi 11": "xiaomi",
        "OnePlus 9": "OnePlus",
    }

    # Default Android version pieces used for spoofing
    ANDROID_VERSION: List[int] = [30, 0, 0]

    # Default parameters used to build a user agent string
    APP_VERSION = "269.0.0.18.75"
    VERSION_CODE = "358800771"
    DPI = "420dpi"
    RESOLUTION = "1080x2400"
    CPU = "qcom"

    @staticmethod
    def generate(model: Optional[str] = None) -> Dict[str, object]:
        """Generate device information for the given model.

        Parameters
        ----------
        model: str, optional
            Specific device model to spoof. If ``None`` a model will be chosen
            randomly from :pyattr:`DEFAULT_MODELS`.

        Returns
        -------
        dict
            Dictionary containing ``manufacturer``, ``model``, ``android_version``
            and ``user_agent`` keys.
        """
        models = list(DeviceGenerator.DEFAULT_MODELS.keys())
        if not model:
            model = random.choice(models)
        manufacturer = DeviceGenerator.DEFAULT_MODELS.get(model, "android")

        android_version = DeviceGenerator.ANDROID_VERSION
        android_release = ".".join(str(v) for v in android_version)

        data = {
            "app_version": DeviceGenerator.APP_VERSION,
            "android_version": android_version[0],
            "android_release": android_release,
            "dpi": DeviceGenerator.DPI,
            "resolution": DeviceGenerator.RESOLUTION,
            "manufacturer": manufacturer,
            "device": model,
            "model": model,
            "cpu": DeviceGenerator.CPU,
            "version_code": DeviceGenerator.VERSION_CODE,
        }
        user_agent = config.USER_AGENT_BASE.format(**data, locale="en_US")

        return {
            "manufacturer": manufacturer,
            "model": model,
            "android_version": android_version,
            "user_agent": user_agent,
        }
