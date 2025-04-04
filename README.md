# Odoo 18 - Technical Test

This repository contains the implementation of a technical test using odoo 18  . The goal is to design and implement region and team management, prospect tracking, and client acquisition within an Odoo 18 module.

---

## 📌 User Stories & Features

### 1. 🌍 Regional Management & Commercial Team Affiliation
- Custom `region` model to manage geographical zones.
- Commercial teams can be linked to a specific region.
- Each team has a **Team Lead** and each region has a **Commercial Lead**.

### 2. 🧑‍💼 Prospect Creation & Assignment
- **Team Leads** can:
  - Create prospects.
  - Assign prospects to themselves or any member of their team.
- **Team Members** can:
  - Create prospects which are automatically assigned to themselves.

### 3. 📊 Prospects Pipeline Management
- Custom pipeline stages:
  - Contact Prospect
  - Offer Sent
  - Won
  - Lost
- Prospects marked as **'Won'** are automatically converted into clients.

### 4. 🧾 Client Info & Acquisition PDF
- Generate a downloadable PDF with:
  - Client information
  - Acquisition history including:
    - Who acquired the client
    - Offer sent date
    - When the client was won

---

## 🛠️ Installation

1. Clone this repository and move the prospect_manager folder to your Odoo `addons` directory:
   ```bash
   git clone https://github.com/issamhamamid/Odoo-prospects-manager.git
   ```

2. Restart your Odoo server:
   ```bash
   ./odoo-bin -u all -d your-database-name
   ```

3. Activate Developer Mode and install the module from the Apps menu.

---

## ✅ Testing

- Head to the Prospect Manager  module menu in the Odoo interface.
- You can see 4 sub menus in there :
  - Regions
  - Teams
  - Prospects
  - Clients
- PDF report generation is available in the client form view.

---


