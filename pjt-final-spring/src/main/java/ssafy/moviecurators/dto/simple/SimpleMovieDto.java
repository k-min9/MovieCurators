package ssafy.moviecurators.dto.simple;

import lombok.Data;
import org.hibernate.annotations.Type;
import ssafy.moviecurators.domain.movies.Movie;

import javax.persistence.Column;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import javax.validation.constraints.Size;
import java.sql.Date;
import java.util.List;

@Data
public class SimpleMovieDto {

    private Long id;
    private String backdrop_path;
    private String poster_path;
    private String overview;
    private Date release_date;
    private String original_title;
    private String title;
    private Double popularity;
    private Integer vote_count;
    private Double vote_average;
    private List<Integer> movie_reference_overview;

    public SimpleMovieDto(Movie movie) {
        this.id = movie.getId();
        this.backdrop_path = movie.getBackdrop_path();
        this.poster_path = movie.getPoster_path();
        this.overview = movie.getOverview();
        this.release_date = movie.getRelease_date();
        this.original_title = movie.getOriginal_title();
        this.title = movie.getTitle();
        this.popularity = movie.getPopularity();
        this.vote_count = movie.getVote_count();
        this.vote_average = movie.getVote_average();
        this.movie_reference_overview = getMovie_reference_overview();
    }
}
