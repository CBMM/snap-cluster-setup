# copy pasted from https://docs.vllm.ai/en/latest/getting_started/quickstart.html

# do export VLLM_USE_MODELSCOPE=True
from vllm import LLM, SamplingParams

def test_vllm():
    prompts = [
        "Hello, my name is",
        "The president of the United States is",
        "The capital of France is",
        "The future of AI is",
    ]
    sampling_params = SamplingParams(temperature=0.8, top_p=0.95)


    llm = LLM(model="facebook/opt-125m")

    outputs = llm.generate(prompts, sampling_params)

    # Print the outputs.
    for output in outputs:
        prompt = output.prompt
        generated_text = output.outputs[0].text
        print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}")

if __name__ == "__main__":
    import time
    start_time = time.time()
    test_vllm()
    print(f"Time taken: {time.time() - start_time:.2f} seconds, or {(time.time() - start_time) / 60:.2f} minutes, or {(time.time() - start_time) / 3600:.2f} hours.\a")