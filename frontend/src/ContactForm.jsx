import { useState } from "react";

const ContactForm =({ existingContact ={} , updateCallback}) => {
    const [firstName, setFirstName] = useState(existingContact.firstName || "")  // states for the form which we will be submitting to the api
    const [lastName, setLastName] = useState(existingContact.lastName || "") // it will check for an existing contact and if we have one it will put the infor on the fields
    const [email, setEmail] = useState(existingContact.email || "")

    const updating = Object.entries(existingContact).length !== 0 // if you pass a object that has atleast one entry in it that means we are updating an existing contact


    
    const onSubmit = async (e) => {  // onSubmit function a POST method request is sent to the backend
        e.preventDefault()  // using the function to prevent the from refreshing repeatedly

        const data = {
            firstName,
            lastName,
            email
        }
        const url = "http://127.0.0.1:5000/"+(updating? `update_contact/${existingContact.id}` : "create_contact") 
        // we are passing some dynamic variable that is using the ? operator we are checking if we are updating and if we are then the url is set to update contact and with the id of the existing contact
        const options ={      // specifying the method and telling the header what type of data is being sent
            method: updating? "PATCH":"POST",
            headers: {
                "Content-Type":"application/json"
            },
            body: JSON.stringify(data)
        }
        const response = await fetch(url, options)  // sending the request to the url with the specified options
        if (response.status !== 201 && response.status !== 200){
            const data = await response.json() //getting the error message from the api response json 
            alert(data.message)
        }else{
            updateCallback()
        }

    }

    // returning a form with firlds for getting the user input for firstname, lastname and the email
    return (
        <form onSubmit={onSubmit}>
            <div>
                <label htmlFor="firstName">First Name:</label>
                <input type="text" 
                id="firstName" 
                value={firstName} 
                onChange={(e) => setFirstName(e.target.value)} />
            </div>
            <div>
                <label htmlFor="lastName">Last Name:</label>
                <input type="text" 
                id="lastName" 
                value={lastName} 
                onChange={(e) => setLastName(e.target.value)} />
            </div>
            <div>
                <label htmlFor="email">Email:</label>
                <input type="text" 
                id="email" 
                value={email} 
                onChange={(e) => setEmail(e.target.value)} />
            </div>
            <button type="submit">{updating?"Update":"Create Contact"}</button>
        </form>
    )
}


export default ContactForm