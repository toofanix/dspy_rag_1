import phoenix as px
from phoenix.otel import register
from openinference.instrumentation.groq import GroqInstrumentor
from openinference.instrumentation.openai import OpenAIInstrumentor
from openinference.instrumentation.dspy import DSPyInstrumentor
from openinference.instrumentation.llama_index import LlamaIndexInstrumentor
from openinference.instrumentation.langchain import LangChainInstrumentor

def launch_app_and_start_project(project_name, llm_provider='dspy'):

    tracer_provider = register(project_name=project_name)

    match llm_provider:
        case 'ollama':
            pass
        case 'groq':
            GroqInstrumentor().instrument(tracer_provider=tracer_provider)
        case "openai":
            OpenAIInstrumentor().instrument(tracer_provider=tracer_provider)
        case "dspy":
            DSPyInstrumentor().instrument(tracer_provider=tracer_provider)
        case "llama_index":
            LlamaIndexInstrumentor().instrument(tracer_provider=tracer_provider)    
        case "langchain":
            LangChainInstrumentor().instrument(tracer_provider=tracer_provider)

    return tracer_provider




