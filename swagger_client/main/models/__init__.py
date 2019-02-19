# coding: utf-8

# flake8: noqa
"""
    crush-main 平台接口（主平台）

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import models into model package
from swagger_client.main.models.account_info_respones import AccountInfoRespones
from swagger_client.main.models.certification_audit import CertificationAudit
from swagger_client.main.models.delete_favoriter_response import DeleteFavoriterResponse
from swagger_client.main.models.delete_project_favorites_response import DeleteProjectFavoritesResponse
from swagger_client.main.models.exchange_coin import ExchangeCoin
from swagger_client.main.models.exchange_coin_buyer_coin import ExchangeCoinBuyerCoin
from swagger_client.main.models.face_id_result_error_response import FaceIdResultErrorResponse
from swagger_client.main.models.face_id_result_response import FaceIdResultResponse
from swagger_client.main.models.face_id_result_response_biz_info import FaceIdResultResponseBizInfo
from swagger_client.main.models.face_id_result_response_idcard_info import FaceIdResultResponseIdcardInfo
from swagger_client.main.models.face_id_result_response_idcard_info_back_side import FaceIdResultResponseIdcardInfoBackSide
from swagger_client.main.models.face_id_result_response_idcard_info_back_side_ocr_result import FaceIdResultResponseIdcardInfoBackSideOcrResult
from swagger_client.main.models.face_id_result_response_idcard_info_front_side import FaceIdResultResponseIdcardInfoFrontSide
from swagger_client.main.models.face_id_result_response_idcard_info_front_side_ocr_result import FaceIdResultResponseIdcardInfoFrontSideOcrResult
from swagger_client.main.models.face_id_result_response_idcard_info_front_side_ocr_result_birthday import FaceIdResultResponseIdcardInfoFrontSideOcrResultBirthday
from swagger_client.main.models.face_id_result_response_idcard_info_front_side_ocr_result_legality import FaceIdResultResponseIdcardInfoFrontSideOcrResultLegality
from swagger_client.main.models.face_id_result_response_images import FaceIdResultResponseImages
from swagger_client.main.models.face_id_result_response_liveness_result import FaceIdResultResponseLivenessResult
from swagger_client.main.models.face_id_result_response_liveness_result_details import FaceIdResultResponseLivenessResultDetails
from swagger_client.main.models.face_id_result_response_liveness_result_face_genuineness import FaceIdResultResponseLivenessResultFaceGenuineness
from swagger_client.main.models.face_id_result_response_verify_result import FaceIdResultResponseVerifyResult
from swagger_client.main.models.face_id_result_response_verify_result_id_exceptions import FaceIdResultResponseVerifyResultIdExceptions
from swagger_client.main.models.face_id_result_response_verify_result_result_faceid import FaceIdResultResponseVerifyResultResultFaceid
from swagger_client.main.models.face_id_result_response_verify_result_result_faceid_thresholds import FaceIdResultResponseVerifyResultResultFaceidThresholds
from swagger_client.main.models.face_id_token_response import FaceIdTokenResponse
from swagger_client.main.models.face_id_url_response import FaceIdUrlResponse
from swagger_client.main.models.get_account_info_response import GetAccountInfoResponse
from swagger_client.main.models.get_all_withdraw_addresses_response import GetAllWithdrawAddressesResponse
from swagger_client.main.models.get_all_withdraw_addresses_response_inner import GetAllWithdrawAddressesResponseInner
from swagger_client.main.models.get_announcements_by_exchange_id_response import GetAnnouncementsByExchangeIdResponse
from swagger_client.main.models.get_announcements_by_exchange_id_response_items import GetAnnouncementsByExchangeIdResponseItems
from swagger_client.main.models.get_announcements_exchange_response import GetAnnouncementsExchangeResponse
from swagger_client.main.models.get_app_version_response import GetAppVersionResponse
from swagger_client.main.models.get_asset_by_coin_id_response import GetAssetByCoinIdResponse
from swagger_client.main.models.get_asset_by_coin_id_response_estimates import GetAssetByCoinIdResponseEstimates
from swagger_client.main.models.get_asset_password_response import GetAssetPasswordResponse
from swagger_client.main.models.get_assets_response import GetAssetsResponse
from swagger_client.main.models.get_assets_response_asset_info import GetAssetsResponseAssetInfo
from swagger_client.main.models.get_assets_response_estimates import GetAssetsResponseEstimates
from swagger_client.main.models.get_balance_by_coin_id_response import GetBalanceByCoinIdResponse
from swagger_client.main.models.get_banner_list_response import GetBannerListResponse
from swagger_client.main.models.get_banner_list_response_items import GetBannerListResponseItems
from swagger_client.main.models.get_coin_by_id_response import GetCoinByIdResponse
from swagger_client.main.models.get_coin_lists_response import GetCoinListsResponse
from swagger_client.main.models.get_coin_lists_response_inner import GetCoinListsResponseInner
from swagger_client.main.models.get_coin_overview_response import GetCoinOverviewResponse
from swagger_client.main.models.get_enterprise_response import GetEnterpriseResponse
from swagger_client.main.models.get_entrusts_exchange_list_response import GetEntrustsExchangeListResponse
from swagger_client.main.models.get_entrusts_exchange_list_response_items import GetEntrustsExchangeListResponseItems
from swagger_client.main.models.get_entrusts_query import GetEntrustsQuery
from swagger_client.main.models.get_entrusts_response import GetEntrustsResponse
from swagger_client.main.models.get_entrusts_response_items import GetEntrustsResponseItems
from swagger_client.main.models.get_exchange_list_response import GetExchangeListResponse
from swagger_client.main.models.get_exchange_list_response_items import GetExchangeListResponseItems
from swagger_client.main.models.get_exchange_market_quotation_response import GetExchangeMarketQuotationResponse
from swagger_client.main.models.get_exchange_market_quotation_response_inner import GetExchangeMarketQuotationResponseInner
from swagger_client.main.models.get_exchange_quotation_response import GetExchangeQuotationResponse
from swagger_client.main.models.get_exchange_quotation_response_inner import GetExchangeQuotationResponseInner
from swagger_client.main.models.get_favoriter_exchange_list_response import GetFavoriterExchangeListResponse
from swagger_client.main.models.get_favoriter_exchange_list_response_items import GetFavoriterExchangeListResponseItems
from swagger_client.main.models.get_favoriter_exchange_list_response_markets import GetFavoriterExchangeListResponseMarkets
from swagger_client.main.models.get_favoriter_list_response import GetFavoriterListResponse
from swagger_client.main.models.get_favoriter_list_response_items import GetFavoriterListResponseItems
from swagger_client.main.models.get_favoriter_market_list_response import GetFavoriterMarketListResponse
from swagger_client.main.models.get_favoriter_market_list_response_items import GetFavoriterMarketListResponseItems
from swagger_client.main.models.get_historical_data_response import GetHistoricalDataResponse
from swagger_client.main.models.get_historical_data_response_inner import GetHistoricalDataResponseInner
from swagger_client.main.models.get_invite_info_response import GetInviteInfoResponse
from swagger_client.main.models.get_invites_list_response import GetInvitesListResponse
from swagger_client.main.models.get_invites_list_response_email_address import GetInvitesListResponseEmailAddress
from swagger_client.main.models.get_invites_list_response_items import GetInvitesListResponseItems
from swagger_client.main.models.get_is_favoriter_response import GetIsFavoriterResponse
from swagger_client.main.models.get_is_favorites_response import GetIsFavoritesResponse
from swagger_client.main.models.get_journals_query import GetJournalsQuery
from swagger_client.main.models.get_journals_response import GetJournalsResponse
from swagger_client.main.models.get_journals_response_items import GetJournalsResponseItems
from swagger_client.main.models.get_kinmall_info_response import GetKinmallInfoResponse
from swagger_client.main.models.get_kinmall_list_response import GetKinmallListResponse
from swagger_client.main.models.get_kinmall_list_response_items import GetKinmallListResponseItems
from swagger_client.main.models.get_kinmall_list_response_query import GetKinmallListResponseQuery
from swagger_client.main.models.get_kinmall_menu_response import GetKinmallMenuResponse
from swagger_client.main.models.get_kinmall_menu_response_items import GetKinmallMenuResponseItems
from swagger_client.main.models.get_kinmall_menu_response_submenu import GetKinmallMenuResponseSubmenu
from swagger_client.main.models.get_listed_market_info_list_response import GetListedMarketInfoListResponse
from swagger_client.main.models.get_listed_market_info_list_response_items import GetListedMarketInfoListResponseItems
from swagger_client.main.models.get_market_list_response import GetMarketListResponse
from swagger_client.main.models.get_market_list_response_items import GetMarketListResponseItems
from swagger_client.main.models.get_market_response import GetMarketResponse
from swagger_client.main.models.get_message_list_response import GetMessageListResponse
from swagger_client.main.models.get_message_list_response_items import GetMessageListResponseItems
from swagger_client.main.models.get_newest_announcement_response import GetNewestAnnouncementResponse
from swagger_client.main.models.get_newest_announcement_response_inner import GetNewestAnnouncementResponseInner
from swagger_client.main.models.get_news_list_response import GetNewsListResponse
from swagger_client.main.models.get_news_list_response_items import GetNewsListResponseItems
from swagger_client.main.models.get_personal_response import GetPersonalResponse
from swagger_client.main.models.get_platform_article_response import GetPlatformArticleResponse
from swagger_client.main.models.get_platform_articles_response import GetPlatformArticlesResponse
from swagger_client.main.models.get_platform_articles_response_items import GetPlatformArticlesResponseItems
from swagger_client.main.models.get_project_announcement_info_response import GetProjectAnnouncementInfoResponse
from swagger_client.main.models.get_project_announcement_list_response import GetProjectAnnouncementListResponse
from swagger_client.main.models.get_project_announcement_list_response_items import GetProjectAnnouncementListResponseItems
from swagger_client.main.models.get_project_favorites_response import GetProjectFavoritesResponse
from swagger_client.main.models.get_project_favorites_response_items import GetProjectFavoritesResponseItems
from swagger_client.main.models.get_project_quotation_response import GetProjectQuotationResponse
from swagger_client.main.models.get_project_quotation_response_inner import GetProjectQuotationResponseInner
from swagger_client.main.models.get_project_report_list_response import GetProjectReportListResponse
from swagger_client.main.models.get_project_report_list_response_items import GetProjectReportListResponseItems
from swagger_client.main.models.get_project_response import GetProjectResponse
from swagger_client.main.models.get_project_response_coin_info import GetProjectResponseCoinInfo
from swagger_client.main.models.get_project_response_project_info import GetProjectResponseProjectInfo
from swagger_client.main.models.get_project_response_project_info_communities import GetProjectResponseProjectInfoCommunities
from swagger_client.main.models.get_project_response_sponsor_info import GetProjectResponseSponsorInfo
from swagger_client.main.models.get_projects_response import GetProjectsResponse
from swagger_client.main.models.get_projects_response_items import GetProjectsResponseItems
from swagger_client.main.models.get_projects_response_query import GetProjectsResponseQuery
from swagger_client.main.models.get_projects_search_response import GetProjectsSearchResponse
from swagger_client.main.models.get_projects_search_response_items import GetProjectsSearchResponseItems
from swagger_client.main.models.get_quotation_list_response import GetQuotationListResponse
from swagger_client.main.models.get_quotation_list_response_inner import GetQuotationListResponseInner
from swagger_client.main.models.get_ranking_list_response import GetRankingListResponse
from swagger_client.main.models.get_ranking_list_response_items import GetRankingListResponseItems
from swagger_client.main.models.get_recharge_addresses_response import GetRechargeAddressesResponse
from swagger_client.main.models.get_recharge_record_query import GetRechargeRecordQuery
from swagger_client.main.models.get_recharge_records_response import GetRechargeRecordsResponse
from swagger_client.main.models.get_recharge_records_response_items import GetRechargeRecordsResponseItems
from swagger_client.main.models.get_rechargeable_lists_response import GetRechargeableListsResponse
from swagger_client.main.models.get_rechargeable_lists_response_inner import GetRechargeableListsResponseInner
from swagger_client.main.models.get_reward_list_response import GetRewardListResponse
from swagger_client.main.models.get_reward_list_response_items import GetRewardListResponseItems
from swagger_client.main.models.get_suggestion_exchange_list_response import GetSuggestionExchangeListResponse
from swagger_client.main.models.get_suggestion_exchange_list_response_inner import GetSuggestionExchangeListResponseInner
from swagger_client.main.models.get_suggestion_market_list_response import GetSuggestionMarketListResponse
from swagger_client.main.models.get_suggestion_market_list_response_items import GetSuggestionMarketListResponseItems
from swagger_client.main.models.get_total_data_response import GetTotalDataResponse
from swagger_client.main.models.get_trades_query import GetTradesQuery
from swagger_client.main.models.get_trades_response import GetTradesResponse
from swagger_client.main.models.get_trades_response_items import GetTradesResponseItems
from swagger_client.main.models.get_tradingpair_precision_response import GetTradingpairPrecisionResponse
from swagger_client.main.models.get_tradingpair_precision_response_inner import GetTradingpairPrecisionResponseInner
from swagger_client.main.models.get_url_response import GetUrlResponse
from swagger_client.main.models.get_withdraw_addresses_response import GetWithdrawAddressesResponse
from swagger_client.main.models.get_withdraw_addresses_response_inner import GetWithdrawAddressesResponseInner
from swagger_client.main.models.get_withdraw_record_query import GetWithdrawRecordQuery
from swagger_client.main.models.get_withdraw_records_response import GetWithdrawRecordsResponse
from swagger_client.main.models.get_withdraw_records_response_items import GetWithdrawRecordsResponseItems
from swagger_client.main.models.get_withdraw_total_response import GetWithdrawTotalResponse
from swagger_client.main.models.get_withdrawable_lists_response import GetWithdrawableListsResponse
from swagger_client.main.models.get_withdrawable_lists_response_inner import GetWithdrawableListsResponseInner
from swagger_client.main.models.getbind_statues_request import GetbindStatuesRequest
from swagger_client.main.models.init_captcha_response import InitCaptchaResponse
from swagger_client.main.models.init_google_request import InitGoogleRequest
from swagger_client.main.models.init_google_response import InitGoogleResponse
from swagger_client.main.models.notify_list import NotifyList
from swagger_client.main.models.notify_list_items import NotifyListItems
from swagger_client.main.models.pagination import Pagination
from swagger_client.main.models.pagination_links import PaginationLinks
from swagger_client.main.models.phone_number import PhoneNumber
from swagger_client.main.models.post_assets_password_check_request import PostAssetsPasswordCheckRequest
from swagger_client.main.models.post_assets_password_check_response import PostAssetsPasswordCheckResponse
from swagger_client.main.models.post_base_token_unauthorized_response import PostBaseTokenUnauthorizedResponse
from swagger_client.main.models.post_bind_google_authenticator_request import PostBindGoogleAuthenticatorRequest
from swagger_client.main.models.post_bind_phone_request import PostBindPhoneRequest
from swagger_client.main.models.post_close_google_authenticator_request import PostCloseGoogleAuthenticatorRequest
from swagger_client.main.models.post_close_phone_authenticator_request import PostClosePhoneAuthenticatorRequest
from swagger_client.main.models.post_code_response import PostCodeResponse
from swagger_client.main.models.post_edit_phone_request import PostEditPhoneRequest
from swagger_client.main.models.post_enterprise_certification_request import PostEnterpriseCertificationRequest
from swagger_client.main.models.post_entrust_response import PostEntrustResponse
from swagger_client.main.models.post_entrusts_request import PostEntrustsRequest
from swagger_client.main.models.post_error_response import PostErrorResponse
from swagger_client.main.models.post_favoriter_exchange_request import PostFavoriterExchangeRequest
from swagger_client.main.models.post_favoriter_market_request import PostFavoriterMarketRequest
from swagger_client.main.models.post_favoriter_request import PostFavoriterRequest
from swagger_client.main.models.post_favoriter_response import PostFavoriterResponse
from swagger_client.main.models.post_file_response import PostFileResponse
from swagger_client.main.models.post_individual_certification_request import PostIndividualCertificationRequest
from swagger_client.main.models.post_login_request import PostLoginRequest
from swagger_client.main.models.post_login_response import PostLoginResponse
from swagger_client.main.models.post_message_enable_request import PostMessageEnableRequest
from swagger_client.main.models.post_open_google_authenticator_request import PostOpenGoogleAuthenticatorRequest
from swagger_client.main.models.post_open_phone_authenticator_request import PostOpenPhoneAuthenticatorRequest
from swagger_client.main.models.post_password_validation_request import PostPasswordValidationRequest
from swagger_client.main.models.post_plat_form_register_request import PostPlatFormRegisterRequest
from swagger_client.main.models.post_project_favorites_request import PostProjectFavoritesRequest
from swagger_client.main.models.post_project_favorites_response import PostProjectFavoritesResponse
from swagger_client.main.models.post_register_request import PostRegisterRequest
from swagger_client.main.models.post_reset_password_request import PostResetPasswordRequest
from swagger_client.main.models.post_reset_phone_unauthorized_response import PostResetPhoneUnauthorizedResponse
from swagger_client.main.models.post_sendverification_code_request import PostSendverificationCodeRequest
from swagger_client.main.models.post_set_password_request import PostSetPasswordRequest
from swagger_client.main.models.post_tenant_favoriter_market_request import PostTenantFavoriterMarketRequest
from swagger_client.main.models.post_unauthorized_account_response import PostUnauthorizedAccountResponse
from swagger_client.main.models.post_unauthorized_response import PostUnauthorizedResponse
from swagger_client.main.models.post_vps_request import PostVPSRequest
from swagger_client.main.models.post_withdraw_address_request import PostWithdrawAddressRequest
from swagger_client.main.models.post_withdraw_request import PostWithdrawRequest
from swagger_client.main.models.postbind_phone_unauthorized_response import PostbindPhoneUnauthorizedResponse
from swagger_client.main.models.postlogin_history_respones import PostloginHistoryRespones
from swagger_client.main.models.postlogin_history_respones_items import PostloginHistoryResponesItems
from swagger_client.main.models.put_assets_password_request import PutAssetsPasswordRequest
from swagger_client.main.models.put_update_vps_request import PutUpdateVPSRequest
from swagger_client.main.models.put_vps_request import PutVPSRequest
from swagger_client.main.models.verify_info import VerifyInfo
from swagger_client.main.models.verify_info_1 import VerifyInfo1
from swagger_client.main.models.verify_request import VerifyRequest
from swagger_client.main.models.verify_response import VerifyResponse
