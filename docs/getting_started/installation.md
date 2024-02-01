# Installation

## Requirements

QuestionPy is a framework developed in Python.
Therefore, you need a compatible Python version installed.
A list of compatible versions can be found [here](faq.md#what-python-version-can-i-use-with-questionpy)

---

## Install QuestionPy SDK

To create your own question type, QuestionPy provides a Software Development Kit (SDK).



[//]: # (Sadly the combination of an enumerated list and code doesn't really work with mkdocs.)

<ol>
    <li><p>Make sure that the Python interpreter can load QuestionPy’s code.
      The most convenient way to do this is to use a virtual environment and <a href="https://pip.pypa.io/en/stable/">pip</a>.</p>
      <p>If you need additional information about creating virtual environments see: 
            <a href="https://docs.python.org/3/library/venv.html#creating-virtual-environments">Creation of virtual environments</a></p>
   </li>
   <li>After creating and activating your virtual environment, you can install the <i>questionpy-sdk</i> code with:
      <br>
      <div style="margin-top:1em;">
         <code style="padding: 1em">pip install git+https://github.com/questionpy-org/questionpy-sdk.git</code>
      </div>
      <br>   
   </li>
   <li>You can verify that <i>questionpy-sdk</i> was successfully installed by running:
      <br>
      <div style="margin-top:1em;">
         <code style="padding: 1em">questionpy-sdk -h</code>
      </div>
      <br>   
      This should display the help section.
   </li>
</ol>
You are now ready to continue with [Create a QuestionType](create_qtype.md).
