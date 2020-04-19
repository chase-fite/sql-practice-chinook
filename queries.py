# 1. Provide a query showing Customers (just their full names, customer ID and country) who are not in the US.
'''SELECT FirstName, LastName, CustomerId, Country
FROM Customer
WHERE Country NOT LIKE "usa";'''

# 2. Provide a query only showing the Customers from Brazil.
'''SELECT FirstName, LastName, CustomerId, Country
FROM Customer
WHERE Country LIKE "brazil";'''

# 3. Provide a query showing the Invoices of customers who are from Brazil. The resultant table should show the customer's full name, Invoice ID, Date of the invoice and billing country.
'''SELECT FirstName, LastName, InvoiceId, BillingCountry AS 'Country'
FROM Customer
JOIN Invoice
ON Customer.CustomerId = Invoice.CustomerId
WHERE Country LIKE "brazil";'''

# 4. Provide a query showing only the Employees who are Sales Agents.
'''SELECT *
FROM Employee
WHERE Title LIKE "%sales%%agent%";'''

# 5. Provide a query showing a unique/distinct list of billing countries from the Invoice table.
'''SELECT DISTINCT BillingCountry AS 'BillingCountries'
FROM Invoice
GROUP BY BillingCountry;'''

# 6. Provide a query that shows the invoices associated with each sales agent. The resultant table should include the Sales Agent's full name.
'''SELECT InvoiceId, Invoice.CustomerId, SupportRepId, Employee.FirstName, Employee.LastName, Title
FROM Invoice
JOIN Customer, Employee
ON Invoice.CustomerId = Customer.CustomerId
AND SupportRepId = Employee.EmployeeId
ORDER BY InvoiceId;'''

# 7. Provide a query that shows the Invoice Total, Customer name, Country and Sale Agent name for all invoices and customers.
'''SELECT InvoiceId, Total, Customer.FirstName AS 'CustomerFirstName', Customer.LastName AS 'CustomerLastName', BillingCountry AS 'Country',
	Employee.FirstName AS 'AgentFirstName', Employee.LastName AS 'AgentLastName'
FROM Invoice
JOIN Customer, Employee
ON Invoice.CustomerId = Customer.CustomerId
AND Customer.SupportRepId = Employee.EmployeeId;'''

# 8. How many Invoices were there in 2009 and 2011?
'''SELECT COUNT(InvoiceId) AS 'InvoiceCount', strftime('%Y', InvoiceDate) AS 'InvoiceYear'
FROM Invoice
WHERE InvoiceYear = '2009'
OR InvoiceYear = '2011'
GROUP BY InvoiceYear;'''

# 9. What are the respective total sales for each of those years?
'''SELECT SUM(Total) AS 'InvoiceTotal', strftime('%Y', InvoiceDate) AS 'InvoiceYear'
FROM Invoice
WHERE InvoiceYear = '2009'
OR InvoiceYear = '2011'
GROUP BY InvoiceYear;'''

# 10. Looking at the InvoiceLine table, provide a query that COUNTs the number of line items for Invoice ID 37.
'''SELECT InvoiceId, SUM(Quantity) AS 'QuantityOfLineItems'
FROM InvoiceLine
WHERE InvoiceId = 37
GROUP BY InvoiceId;'''

# 11. Looking at the InvoiceLine table, provide a query that COUNTs the number of line items for each Invoice. HINT: GROUP BY
'''SELECT InvoiceId, COUNT(Quantity) AS 'QuantityOfLineItems'
FROM InvoiceLine
GROUP BY InvoiceId;'''

# 12. Provide a query that includes the purchased track name with each invoice line item.
'''SELECT InvoiceLineId, InvoiceId, InvoiceLine.TrackId, Name AS 'TrackName', InvoiceLine.UnitPrice, Quantity
FROM InvoiceLine
JOIN Track
ON InvoiceLine.TrackId = Track.TrackId
ORDER BY InvoiceLineId;'''

# 13. Provide a query that includes the purchased track name AND artist name with each invoice line item.
'''SELECT InvoiceLineId, InvoiceId, InvoiceLine.TrackId, Track.Name AS 'TrackName', Artist.Name AS 'ArtistName', InvoiceLine.UnitPrice, Quantity
FROM InvoiceLine
JOIN Track, Album, Artist
ON InvoiceLine.TrackId = Track.TrackId
AND Track.AlbumId = Album.AlbumId
AND Album.ArtistId = Artist.ArtistId
ORDER BY InvoiceLineId;'''

# 14. Provide a query that shows the # of invoices per country.
'''SELECT COUNT(InvoiceId) AS 'NumberOfInvoices', BillingCountry AS 'Country'
FROM Invoice
GROUP BY BillingCountry;'''

# 15. Provide a query that shows the total number of tracks in each playlist. The Playlist name should be include on the resulant table.
'''SELECT PlaylistTrack.PlaylistId, Playlist.Name, COUNT(TrackId) AS 'NumberOfTracks'
FROM PlaylistTrack
JOIN Playlist
ON PlaylistTrack.PlaylistId = Playlist.PlaylistId
GROUP BY PlaylistTrack.PlaylistId;'''

# 16. Provide a query that shows all the Tracks, but displays no IDs. The result should include the Album name, Media type and Genre.
'''SELECT Track.Name AS 'TrackName', Album.Title AS 'AlbumTitle', MediaType.Name AS 'MediaType', Genre.Name AS 'Genre'
FROM Track
JOIN Album, MediaType, Genre
ON Track.AlbumId = Album.AlbumId
AND Track.MediaTypeId = MediaType.MediaTypeId
AND Track.GenreId = Genre.GenreId;'''

# 17. Provide a query that shows all Invoices but includes the # of invoice line items.
'''SELECT Invoice.*, COUNT(InvoiceLine.InvoiceLineId) AS 'NumberOfLineItems'
FROM Invoice
JOIN InvoiceLine
ON Invoice.InvoiceId = InvoiceLine.InvoiceId
GROUP BY Invoice.InvoiceId;'''

# 18. Provide a query that shows total sales made by each sales agent.
'''SELECT Employee.FirstName, Employee.LastName, Employee.Title, ROUND(SUM(Invoice.Total), 2) AS 'TotalSales'
FROM Invoice
JOIN Customer, Employee
ON Invoice.CustomerId = Customer.CustomerId
AND Customer.SupportRepId = Employee.EmployeeId
GROUP BY Employee.EmployeeId;'''

# 19. Which sales agent made the most in sales in 2009?
'''SELECT SalesAgent, MAX(TotalSales) AS 'TotalSales2009'
FROM (
	SELECT Employee.FirstName || " " || Employee.LastName AS 'SalesAgent', SUM(Invoice.Total) AS 'TotalSales'
	FROM Invoice
	JOIN Customer, Employee
	ON Invoice.CustomerId = Customer.CustomerId
	AND Customer.SupportRepId = Employee.EmployeeId
	WHERE strftime('%Y', Invoice.InvoiceDate) = '2009'
	GROUP BY Employee.EmployeeId
);'''

# 20. Which sales agent made the most in sales over all?
'''SELECT SalesAgent, ROUND(MAX(TotalSales), 2) AS 'TotalSales2009'
FROM (
	SELECT Employee.FirstName || " " || Employee.LastName AS 'SalesAgent', SUM(Invoice.Total) AS 'TotalSales'
	FROM Invoice
	JOIN Customer, Employee
	ON Invoice.CustomerId = Customer.CustomerId
	AND Customer.SupportRepId = Employee.EmployeeId
	GROUP BY Employee.EmployeeId
);'''

# 21. Provide a query that shows the count of customers assigned to each sales agent.
'''SELECT SupportRepId, Employee.FirstName, Employee.LastName, COUNT(CustomerId) AS 'NumberOfCustomers'
FROM Customer
JOIN Employee
ON Customer.SupportRepId = Employee.EmployeeId
GROUP BY SupportRepId;'''

# 22. Provide a query that shows the total sales per country.
'''SELECT BillingCountry AS 'Country', SUM(Total) AS 'TotalSales'
FROM Invoice
GROUP BY BillingCountry;'''

# 23. Which country's customers spent the most?
'''SELECT BillingCountry AS 'Country', MAX(TotalSales) AS 'TotalSales'
FROM (
	SELECT BillingCountry, SUM(Total) AS 'TotalSales'
	FROM Invoice
	GROUP BY BillingCountry
);'''

# 24. Provide a query that shows the most purchased track of 2013.
'''SELECT Name AS 'TrackName', MAX(TracksSold) AS 'NumberSold' 
FROM (
	SELECT COUNT(InvoiceLineId) AS 'TracksSold', InvoiceLine.TrackId, Track.Name, InvoiceLine.Quantity
	FROM InvoiceLine
	JOIN Track
	ON InvoiceLine.TrackId = Track.TrackId
	GROUP BY InvoiceLine.TrackId
);'''

# 25. Provide a query that shows the top 5 most purchased tracks over all.
'''SELECT COUNT(InvoiceLineId) AS 'TracksSold', InvoiceLine.TrackId, Track.Name AS 'TrackName'
FROM InvoiceLine
JOIN Track
ON InvoiceLine.TrackId = Track.TrackId
GROUP BY InvoiceLine.TrackId
ORDER BY TracksSold DESC
LIMIT 5;'''

# 26. Provide a query that shows the top 3 best selling artists.
'''SELECT Artist.Name AS 'ArtistName', ROUND(SUM(InvoiceLine.UnitPrice * InvoiceLine.Quantity), 2) AS 'MoneySpent'
FROM InvoiceLine
JOIN Track, Album, Artist
ON InvoiceLine.TrackId = Track.TrackId
AND Track.AlbumId = Album.AlbumId
AND Album.ArtistId = Artist.ArtistId
GROUP BY Artist.Name
ORDER BY MoneySpent DESC
LIMIT 3;'''

# 27. Provide a query that shows the most purchased Media Type.
'''SELECT MediaType.Name AS 'MediaType', ROUND(SUM(InvoiceLine.UnitPrice * InvoiceLine.Quantity), 2) AS 'MoneySpent'
FROM InvoiceLine
JOIN Track, MediaType
ON InvoiceLine.TrackId = Track.TrackId
AND Track.MediaTypeId = MediaType.MediaTypeId
GROUP BY MediaType.Name
ORDER BY MoneySpent DESC
LIMIT 1;'''