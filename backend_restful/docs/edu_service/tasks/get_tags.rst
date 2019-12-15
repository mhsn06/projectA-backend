==========
tags
==========

It return a list of tags under a designation

*  **URL Params**

No url params

* **Data Params**
.. code-block:: JSON

  {
    "task_id" : "tags",
    "data" : {
        "associated":"//the id of the institute, type string",
        "designation":"//the id of the designation, type string"
    }
  }

* **Success Response:**

When successfully stored associations data in database

* **Code:** 200
* **Content:**
.. code-block:: JSON

  {
    "...":"TODO"
  }

* **Error Response:**

When failed to store associations

* **Code:** 200
* **Content:**
.. code-block:: JSON

  {
    "...":"TODO"
  }

* **Sample Call:**
.. code-block:: javascript

  $.ajax({
  url: "/service_request",
  dataType: "json",
  type : "POST",
  contentType: 'application/json',
  beforeSend: function (xhr) {
    xhr.setRequestHeader ("Authorization", "Token " + "<your token here>");
  },
  data: JSON.stringify({
    "service_name": "education",
    "task":   {
        "task_id" : "tags",
        "data" : {
            "associated":"5ddd62ffd8639286d599dcd6",
            "designation":"5ddd62ffd8639286d599dcd7"
        }
    }
  }),
  success : function(r) {
      console.log(r);
  }
  });

* **Notes:**

No additional notes
