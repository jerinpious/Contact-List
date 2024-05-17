import { useState, useEffect } from 'react'
import './App.css'
import ContactList from './ContactList'
import ContactForm from './ContactForm'

function App() {
  const [contacts, setContacts] = useState([])  // setting up state to set up the constacts
  const [isModalOpen, setIsModalOpen] = useState(false) // we are going to use something called a modal to make the form in such a way that the form will only appear if the create contact or the update button is pressed
  const [currentContact, setCurrentContact ] = useState({})

  useEffect(() => {
    fetchContacts()
  }, []) // so as sooon as the useEffect components renders the fetchContacts function is called

  const fetchContacts = async () => { // we are sending a get request to the backend
    const response = await fetch("http://127.0.0.1:5000/contacts") // we will send a request to the backend to get the contacts 
    const data = await response.json() // once it get the response we will fetch the json data from the data
    setContacts(data.contacts) //will grab the contacts property and set the data 
    console.log(data.contacts)
  }

  const closeModal = () => {
    setIsModalOpen(false)
    setCurrentContact({})
  }

  const openCreateModal = () =>{
    if(!isModalOpen) setIsModalOpen(true)

  }

  const openEditModal = (contact) => {
    if(isModalOpen) return
    setCurrentContact(contact)
    setIsModalOpen(true)

  }

  const onUpdate = () => {
    closeModal()
    fetchContacts()
  }

  return ( // rendering the diffrent components to the page
  <>
    <ContactList contacts={contacts} updateContact={openEditModal} updateCallback={onUpdate}/>  
    <button onClick={openCreateModal}>Create New Contact</button>
    {
      isModalOpen && <div className='Modal'>
        <div className='modal-content'>
          <span className='close' onClick={closeModal}>&times;</span>
          <ContactForm existingContact={currentContact} updateCallback={onUpdate}/>
        </div>

      </div>
    }
    
  </>
  )
}

export default App
