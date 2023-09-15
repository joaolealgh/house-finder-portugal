# Find the best house based on your location, distance to job, distance to shops and other information

## Steps

- Focus on a specific city in Portugal (Lisbon, Porto, Coimbra, etc)

- Web scraping real estate market websites
    - Idealista (https://www.idealista.pt/)
    - Imovirtual (https://www.imovirtual.com/)
    - Supercasa (https://supercasa.pt/)
    - Comprarcasa (https://www.comprarcasa.pt/imoveis)
    - Sapo (https://casa.sapo.pt/)
    - etc...

- Extract relevant information from the web scrape
    - Real estate market website where the house is announced
    - House price
    - Rent price
    - Location (GPS Coordinates, approximate location/zone or if possible the real location, Street name)
    - House/Apartment type (T0, T1, T2, etc)
    - Square footage (Brute Area)
    - Owner contact (phone number, email, whatsapp, etc)
    - Additional conditions (number of upfront rents, deposit, collateral, etc)
    - (Photos, if possible)

- Save the information in a database
    - PostgreSQL database
    - Create ER diagram

- Find most relevant POI's
    - Schools
    - Hospitals
    - Malls
    - Subway stations
    - Gyms
    - Bars
    - Entertainment (Theatre, Movies, etc)
    - etc

- Store the POI's information in a database
    - Location
    - Other relevant information


...