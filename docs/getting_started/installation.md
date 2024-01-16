# Installation

## Requirements

QuestionPy is a framework developed in Python.
Therefore, you need a compatible Python version installed.
A list of compatible versions can be found [here](faq.md#what-python-version-can-i-use-with-questionpy)

---

## Install QuestionPy SDK

To create your own question type, QuestionPy provides a Software Development Kit (SDK).
To install the SDK, you have to clone the QuestionPy SDK development branch from Git.


[//]: # (Sadly the combination of an enumerated list and code doesn't really work with mkdocs.)

<ol>
   <li>Make sure you have <a href="https://git-scm.com/">Git</a> installed before you continue.</li>
   <li>Clone the development branch into a local directory:
      <br>
      <div style="margin-top:1em;">
         <code style="padding: 1em">git clone https://github.com/questionpy-org/questionpy-sdk.git</code>
      </div>
      <br>
      This will create a <b>questionpy-sdk</b> directory in your current directory.
   </li>
   <li>Make sure that the Python interpreter can load QuestionPy’s code.
      The most convenient way to do this is to use a virtual environment and <a href="https://pip.pypa.io/en/stable/">pip</a>.
   </li>
   <li>After creating and activating your virtual environment, you can install the <i>questionpy-sdk</i> code with:
      <br>
      <div style="margin-top:1em;">
         <code style="padding: 1em">pip install -e questionpy-sdk</code>
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
