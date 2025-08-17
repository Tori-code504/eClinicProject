# eClinic - Queue and Record Management System

## Project Overview
eClinic is a healthcare system that streamlines **patient registration, appointments, queue management, and medical records tracking**.  
It is designed to reduce long queues, improve coordination between patients and medical staff, and ensure secure access to medical history.  

---

## Features
- **User Roles**: Admin, Doctor, Nurse, Patient  
- **Patient Management**: Registration, profiles, personal details  
- **Appointment Scheduling**: Book, confirm, or cancel appointments  
- **Queue System**: Organizes patient flow in real-time  
- **Medical Records**: Patient history, diagnoses, prescriptions, and treatments  
- **Authentication & Access Control**: Role-based permissions (Django Groups & Permissions)  
- **Secure Data Handling**: Follows best practices for healthcare data management  

---

## Tech Stack
- **Backend**: Django, Django REST Framework (API support)  
- **Database**: PostgreSQL (recommended) / SQLite (development)  
- **Authentication**: Django Auth with JWT or session-based authentication  
- **Frontend (optional)**: React / Vue / Django Templates  
- **Deployment**: Docker, Heroku / AWS / Render (future plan)  

---

## Project Structure (planned)

---

## Data Models (Planned)

### 1. **User (Extended AbstractUser)**
- Name  
- Phone number  
- Email  
- Role (Patient, Doctor, Nurse, Admin)  

### 2. **PatientProfile**
- Linked to User  
- Date of Birth  
- Gender  
- ID/Passport number  
- Address  

### 3. **Appointment**
- Patient (FK → User/PatientProfile)  
- Doctor (FK → User)  
- Clinic (FK → Clinic/Department)  
- Service type (Consultation, Checkup, Emergency, etc.)  
- Appointment time  
- Status (Pending, Confirmed, Cancelled)  

### 4. **QueueEntry**
- Appointment (FK → Appointment)  
- Queue number  
- Status (Waiting, In-progress, Completed, Skipped)  

### 5. **MedicalRecord**
- Patient (FK → PatientProfile)  
- Doctor (FK → User)  
- Diagnosis  
- Prescription  
- Treatment notes  
- Date created  

