from setuptools import setup

setup(
    name="electrum-server",
    version="0.9",
    scripts=['run_electrum_server','electrum-server'],
    install_requires=['plyvel','jsonrpclib'],
    py_modules=[
        'electrumserver.__init__',
        'electrumserver.utils',
        'electrumserver.storage',
        'electrumserver.deserialize',
        'electrumserver.networks',
        'electrumserver.blockchain_processor',
        'electrumserver.processor',
        'electrumserver.version',
        'electrumserver.irc',
        'electrumserver.stratum_tcp',
        'electrumserver.stratum_http'
    ],
    description="Litecoin Electrum Server",
    author="Thomas Voegtlin",
    author_email="thomasv1@gmx.de",
    license="GNU Affero GPLv3",
    url="https://github.com/pooler/electrum-ltc-server/",
    long_description="""Server for the Electrum Lightweight Litecoin Wallet"""
)


