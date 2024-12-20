# -*- coding: utf-8 -*-
"""FetchEffInc.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1luzrd127mjCBk4UKg95PZyH9umMPIvLV
"""

pip install llama-parse

import nest_asyncio
nest_asyncio.apply()

import os
os.environ["LLAMA_CLOUD_API_KEY"] = "llx-5IXvL83RQwHroB76rpTOUAk7V68nMNPpitrEYXELWmOParpd"

from llama_parse import LlamaParse
document = LlamaParse(result_type="markdown", verbose=True, language="en").load_data("/content/Apartment_Multi-Tenant_Inc_Exp.pdf")

file_name = "Apartment_Multi-Tenant_Inc_Exp.md"
with open(file_name,'w') as file:
  file.write(document[0].text)

parse_instruction = "The provided document is a Income and Expense Document. Provide the Effective Gross Income for year 2011"
documents_with_instruction = LlamaParse(result_type="markdown",
                                        parsing_instruction=parse_instruction
                                        ).load_data("/content/Apartment_Multi-Tenant_Inc_Exp.pdf")

print(documents_with_instruction)