create or replace function insert_book(new_book book, new_author text default null)
returns numeric
language plpgsql
as
$$
begin
    new_book.id := nextval(book_seq);

    if new_author is not null then
        new_book.author_id := get_author_id(new_author);
    end if;

    insert into book values (new_book.*);

    return new_book.id;
end
$$;
