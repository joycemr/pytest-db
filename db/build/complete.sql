drop table if exists author cascade;

create table author (
    id numeric not null,
    f_name text,
    l_name text,
    email text,
    primary key (id)
);

create sequence author_seq
owned by author.id;

drop table if exists book cascade;

create table book (
    id numeric not null,
    author_id numeric,
    title text,
    primary key (id),
    constraint author_fk
        foreign key(author_id)
        references author(id)
);

create sequence book_seq
owned by book.id;

create or replace function get_author(title text)
returns text
language plpgsql
as
$$
declare
    _author text;
begin
    select concat(f_name, ' ',l_name) into _author
    from author
    where id = (
        select author_id
        from book
        where book.title = get_author.title
    );
    return _author;
end
$$;

create or replace function get_author_id(author_name text)
returns numeric
language plpgsql
as
$$
declare
    _id numeric;
    _f_name text;
    _l_name text;
begin
    _f_name := split_part(author_name,' ',1);
    _l_name := split_part(author_name,' ',2);

    select id into _id
    from author
    where f_name = _f_name
      and l_name = _l_name;

    return _id;
end
$$;

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

