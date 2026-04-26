import streamlit as st
from langchain_groq import ChatGroq
from langchain.chains import LLMMathChain, LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.agents.agent_types import AgentType
from langchain.agents import Tool, initialize_agent
from langchain.callbacks import StreamlitCallbackHandler


st.set_page_config(page_title="Text to Math Problem Solver", page_icon="🧮", layout="wide")
st.title("Math Problem Solver Using Groq")

groq_api_key = st.sidebar.text_input("Enter your Groq API Key", type="password")

if not groq_api_key:
    st.info("Please add your Groq API Key in the sidebar to continue.")

else:
    llm = ChatGroq(model='llama-3.1-8b-instant', groq_api_key=groq_api_key)

    wikipedia_wrapper = WikipediaAPIWrapper()
    wikipedia_tool = Tool(
        name='Wikipedia',
        func=wikipedia_wrapper.run,
        description='Use this tool to get information about anything from the internet'
    )

    math_chain = LLMMathChain.from_llm(llm=llm)
    calculator_tool = Tool(
        name='Calculator',
        func=math_chain.run,
        description='Use this tool to perform any mathematical calculations'
    )

    prompt = """
    You are an agent tasked for solving users mathematical question. Logically arrive at the solution
    and display it step wise to the user.

    Question:{question}
    Answer:
    """
    prompt_template = PromptTemplate(input_variables=["question"], template=prompt)
    chain = LLMChain(llm=llm, prompt=prompt_template)

    reasoning_tool = Tool(
        name='Reasoning',
        func=chain.run,
        description='Use this tool to reason through and solve mathematical word problems'
    )

    assistant_agent = initialize_agent(
        tools=[wikipedia_tool, calculator_tool, reasoning_tool],
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        handle_parsing_errors=True
    )

    if 'messages' not in st.session_state:
        st.session_state['messages'] = [
            {'role': 'assistant', 'content': "Hi, I'm your Math Problem Solver. How can I help you?"}
        ]

    for msg in st.session_state.messages:
        st.chat_message(msg['role']).write(msg['content'])

    question = st.text_area("Enter your question:")

    if st.button("Find my answer"):
        if question:
            with st.spinner("Generating response..."):
                st.session_state.messages.append({'role': 'user', 'content': question})
                st.chat_message('user').write(question)

                st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
                response = assistant_agent.run(question, callbacks=[st_cb])  # ✅ pass question, not messages

                st.session_state.messages.append({'role': 'assistant', 'content': response})
                st.write('### Response')
                st.success(response)
        else:
            st.error("Please enter a question")