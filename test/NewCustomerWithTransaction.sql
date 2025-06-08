CREATE OR REPLACE PROCEDURE NewCustomerWithTransaction(
    IN newname character,
    IN newareacode character,
    IN newphone character,
    IN artistname character,
    IN worktitle character,
    IN workcopy character,
    IN price integer,
    IN newSecondName character
)
LANGUAGE 'plpgsql'
AS $BODY$
DECLARE
    tid int;
    aid int;
    rowcount int;
    artistCursor CURSOR FOR
        SELECT artistid FROM ARTIST WHERE Name = artistname;  
BEGIN

    BEGIN;
    
    SELECT COUNT(*) INTO rowcount
    FROM CUSTOMER
    WHERE Name = newName AND Area_Code = newAreaCode AND Phone_Number = newPhone;
    
    IF rowcount > 0 THEN
        RAISE NOTICE 'Клиент с такими данными уже существует';
    
        ROLLBACK;
        RETURN;
    END IF;

    INSERT INTO CUSTOMER(CustomerID, Name, Area_Code, Phone_Number, SecondName)
    VALUES(nextval('CustID'), newName, newAreaCode, newPhone, newSecondName);

    SELECT ArtistID INTO aid
    FROM ARTIST
    WHERE Name = artistName;
    IF aid IS NOT NULL THEN
        SELECT WorkID INTO tid
        FROM WORK
        WHERE Title = workTitle AND Copy = workCopy AND ArtistID = aid;
        
    
        IF tid IS NOT NULL THEN
            INSERT INTO TRANSACTION(TransactionID, CustomerID, WorkID, SalesPrice, PurchaseDate, DateAcquired)
            VALUES(nextval('TransID'), currval('CustID'), tid, price, current_date, current_date);
            IF NOT EXISTS (
                SELECT 1 FROM CUSTOMER_ARTIST_INT WHERE artistid = aid AND customerid = currval('CustID')
            ) THEN
                INSERT INTO CUSTOMER_ARTIST_INT(artistid, customerid)
                VALUES(aid, currval('CustID'));
            END IF;

            RAISE NOTICE 'Новая транзакция добавлена для клиента';
            FOR artist IN artistCursor LOOP
            
                IF NOT EXISTS (
                    SELECT 1 FROM CUSTOMER_ARTIST_INT WHERE artistid = artist.artistid AND customerid = currval('CustID')
                ) THEN
                    INSERT INTO CUSTOMER_ARTIST_INT(customerid, artistid)
                    VALUES(currval('CustID'), artist.artistid);
                END IF;
            END LOOP;
        ELSE
            RAISE NOTICE 'Не найдено произведение для данного художника';
            ROLLBACK;
        END IF;
    ELSE
        RAISE NOTICE 'Не найдено подходящего художника';
        ROLLBACK;
    END IF;
    COMMIT;

EXCEPTION
    WHEN OTHERS THEN
        RAISE NOTICE 'Ошибка: %', SQLERRM;
        ROLLBACK;
END;
$BODY$;
