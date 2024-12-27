from distutils.core import setup

setup(
    name='Open Co-pilot',
    version='0.0.0',
    packages=['core', 'core.gui', 'core.agent', 'core.audio', 'core.screen', 'mem0', 'mem0.llms', 'mem0.llms.utils',
              'mem0.proxy', 'mem0.client', 'mem0.memory', 'mem0.configs', 'mem0.configs.llms',
              'mem0.configs.embeddings', 'mem0.configs.vector_stores', 'mem0.embeddings', 'mem0.vector_stores', 'tools',
              'embedchain', 'embedchain.llm', 'embedchain.bots', 'embedchain.core', 'embedchain.core.db',
              'embedchain.store', 'embedchain.utils', 'embedchain.config', 'embedchain.config.llm',
              'embedchain.config.embedder', 'embedchain.config.vectordb', 'embedchain.config.evaluation',
              'embedchain.memory', 'embedchain.models', 'embedchain.helpers', 'embedchain.loaders',
              'embedchain.chunkers', 'embedchain.embedder', 'embedchain.vectordb', 'embedchain.telemetry',
              'embedchain.evaluation', 'embedchain.evaluation.metrics', 'embedchain.data_formatter'],
    url='',
    license='',
    author='Dawood Touseef',
    author_email='tdawood140@gmail.com',
    description=''
)
