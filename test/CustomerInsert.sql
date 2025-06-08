CREATE OR REPLACE procedure CustomerInsert (
	newName IN char,
	newAreaCode IN char,
	newPhone IN char,
	artistNationality IN char
) AS $func$
DECLARE
	artistCursor CURSOR for
	SELECT ArtistID from ARTIST
	WHERE nationality = artistNationality;
	rowcount int;
BEGIN
	SELECT Count(*) INTO rowcount
	FROM CUSTOMER
	WHERE name = newName AND area_code = newAreaCode AND phone_number = newPhone;

	IF rowcount > 0 THEN
		BEGIN
			raise notice 'Клиент уже есть в базе данных - никаких действий не предпринято';
			RETURN;
		END;
	END IF;

	INSERT INTO CUSTOMER(CustomerID, Name, Area_Code, Phone_Number)
	VALUES(nextval('CustID'), newName, newAreaCode, newPhone);

	FOR artist IN artistCursor LOOP
		INSERT INTO CUSTOMER_ARTIST_INT(customerid , artistid)
		values(currval('CustID'), artist.artistid);
	END LOOP;
	
	raise notice 'Новый клиент успешно добавлен в базу';
END;
$func$ language plpgsql;
