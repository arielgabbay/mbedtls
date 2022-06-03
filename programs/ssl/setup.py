from setuptools import setup, Extension

other_progs = [
        "test/query_config.o", "ssl/ssl_test_lib.o", "../tests/src/helpers.o",
        "../tests/src/asn1_helpers.o", "../tests/src/psa_crypto_helpers.o",
        "../tests/src/psa_exercise_key.o", "../tests/src/threading_helpers.o",
        "../tests/src/random.o", "../tests/src/fake_external_rng_for_test.o",
        "../tests/src/certs.o", "../tests/src/drivers/test_driver_aead.o",
        "../tests/src/drivers/test_driver_asymmetric_encryption.o",
        "../tests/src/drivers/test_driver_signature.o",
        "../tests/src/drivers/test_driver_key_management.o",
        "../tests/src/drivers/test_driver_cipher.o", "../tests/src/drivers/hash.o",
        "../tests/src/drivers/test_driver_mac.o", "../tests/src/drivers/platform_builtin_keys.o"]
cflags = ["-Wall", "-Wextra", "-Wformat=2", "-Wno-format-nonliteral", "-D_FILE_OFFSET_BITS=64", "-O2"]
# extra_link_args = ["-lmbedtls", "-lmbedx509", "-lmbedcrypto"]
extra_link_args = []
libraries = ["mbedtls", "mbedx509", "mbedcrypto"]
include_dirs = ["../tests/include", "../include", "../3rdparty/everest/include",
    "../3rdparty/everest/include/everest", "../3rdparty/everest/include/everest/kremlib", "../library"]
library_dirs = ["../library"]
sources = [prog[:-1] + "c" for prog in other_progs]
sources += ["ssl/ssl_client_python.c"]

setup(
        name="ssl_client",
        version="1",
        author="RnA",
        author_email="sherutishi@btl.gov.il",
        description="SSL client for queries",
        license="GPL-2",
        ext_modules=[
            Extension("ssl_client", sources=sources,
                include_dirs=include_dirs, library_dirs=library_dirs, extra_compile_args=cflags,
                libraries=libraries,
                extra_link_args=extra_link_args)
        ],
)
